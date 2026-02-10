import uvicorn
import requests
import json
import logging
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import Dict, Any

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Africa Geopolitical Risk API")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 設定 ---
GDELT_URL = "https://api.gdeltproject.org/api/v2/geo/geo?query=location:Africa%20theme:ARMEDCONFLICT&mode=PointData&format=geojson"
DATA_FILE = "africa_data.json"
CACHE_DURATION_MINUTES = 15

# --- インメモリキャッシュ ---
data_cache: Dict[str, Any] = {
    "timestamp": None,
    "data": None
}

def get_risk_level(properties: dict) -> str:
    """簡易リスク判定"""
    title = properties.get('name', '').lower()
    if any(x in title for x in ['kill', 'dead', 'bomb', 'blast']):
        return "Critical"
    elif any(x in title for x in ['attack', 'fight', 'clash']):
        return "High"
    else:
        return "Medium"

def fetch_gdelt_data():
    """GDELTからデータを取得"""
    try:
        logger.info("Fetching data from GDELT...")
        response = requests.get(GDELT_URL, timeout=10)
        response.raise_for_status()
        geojson = response.json()

        processed_features = []
        for feature in geojson.get('features', []):
            props = feature.get('properties', {})
            props['risk_level'] = get_risk_level(props)
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
    """リスク情報（GDELT）を取得"""
    global data_cache
    now = datetime.now()

    if (data_cache["data"] is not None and 
        data_cache["timestamp"] is not None and 
        (now - data_cache["timestamp"]) < timedelta(minutes=CACHE_DURATION_MINUTES)):
        return data_cache["data"]

    data = fetch_gdelt_data()
    if data:
        data_cache["data"] = data
        data_cache["timestamp"] = now
        return data
    
    if data_cache["data"]:
        return data_cache["data"]

    raise HTTPException(status_code=503, detail="External API unavailable")

@app.get("/api/countries")
def get_country_data():
    """
    静的な国データをJSONファイルから読み込んで返す
    """
    try:
        if not os.path.exists(DATA_FILE):
            logger.warning("Data file not found, returning empty.")
            return {}
            
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"Error reading country data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
