import uvicorn
import requests
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import Dict, Any

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Africa Geopolitical Risk API")

# CORS設定: フロントエンド(localhost等)からのアクセスを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では特定のドメインに絞るべきです
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 設定 ---
# GDELT GeoJSON API (アフリカの武力衝突)
GDELT_URL = "https://api.gdeltproject.org/api/v2/geo/geo?query=location:Africa%20theme:ARMEDCONFLICT&mode=PointData&format=geojson"
CACHE_DURATION_MINUTES = 15

# --- インメモリキャッシュ ---
# 本番ではRedis等を使用しますが、今回は簡易的な変数キャッシュを使用
data_cache: Dict[str, Any] = {
    "timestamp": None,
    "data": None
}

def get_risk_level(properties: dict) -> str:
    """
    GISスペシャリストの視点:
    メタデータに基づいて簡易的なリスクレベルを判定するロジック。
    （GDELTのソース数や言及数などを元にするのが一般的ですが、
    GeoJSONエンドポイントは情報が限られるため、今回はシミュレーションとして付与します）
    """
    # 実際にはここに複雑なスコアリングロジックが入ります
    # 例: 記事タイトルに "Kill", "Attack" が含まれる場合は High
    title = properties.get('name', '').lower()
    if any(x in title for x in ['kill', 'dead', 'bomb', 'blast']):
        return "Critical"
    elif any(x in title for x in ['attack', 'fight', 'clash']):
        return "High"
    else:
        return "Medium"

def fetch_gdelt_data():
    """GDELTからデータを取得し、整形して返す"""
    try:
        logger.info("Fetching data from GDELT...")
        response = requests.get(GDELT_URL, timeout=10)
        response.raise_for_status()
        geojson = response.json()

        # データ加工: リスクレベルの付与とプロパティの整理
        processed_features = []
        for feature in geojson.get('features', []):
            props = feature.get('properties', {})
            
            # リスクレベルの計算
            risk_level = get_risk_level(props)
            
            # プロパティの拡張
            props['risk_level'] = risk_level
            props['processed_at'] = datetime.now().isoformat()
            
            feature['properties'] = props
            processed_features.append(feature)

        geojson['features'] = processed_features
        return geojson

    except Exception as e:
        logger.error(f"Error fetching GDELT data: {e}")
        return None

@app.get("/")
def root():
    return {"message": "Africa Geopolitical Risk API is running."}

@app.get("/api/risks")
def get_risks():
    """
    リスク情報を取得するエンドポイント
    キャッシュが有効ならキャッシュを返し、期限切れなら再取得する
    """
    global data_cache
    now = datetime.now()

    # キャッシュチェック
    if (data_cache["data"] is not None and 
        data_cache["timestamp"] is not None and 
        (now - data_cache["timestamp"]) < timedelta(minutes=CACHE_DURATION_MINUTES)):
        
        logger.info("Serving from cache")
        return data_cache["data"]

    # 新規取得
    data = fetch_gdelt_data()
    
    if data:
        data_cache["data"] = data
        data_cache["timestamp"] = now
        return data
    
    # 取得失敗時、キャッシュがあれば古くてもそれを返す（フォールバック）
    if data_cache["data"]:
        logger.warning("Fetch failed, serving stale cache")
        return data_cache["data"]

    # 完全な失敗
    raise HTTPException(status_code=503, detail="External API unavailable")

if __name__ == "__main__":
    # 開発用サーバー起動
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
