import json
import os
import datetime
from openai import OpenAI

# --- 設定 ---
# ターゲットとする国コード（コスト節約のため主要国に絞ることも可能）
TARGET_COUNTRIES = [
    "DZA", "AGO", "BEN", "BWA", "BFA", "BDI", "CMR", "CAF", "TCD", "COD", "COG", 
    "CIV", "DJI", "EGY", "GNQ", "ERI", "ETH", "GAB", "GHA", "GIN", "KEN", "LBR", 
    "LBY", "MDG", "MLI", "MAR", "MOZ", "NAM", "NER", "NGA", "RWA", "SEN", "SLE", 
    "SOM", "ZAF", "SSD", "SDN", "TZA", "TGO", "TUN", "UGA", "ZMB", "ZWE"
]

# 基本データ（不変部分）
BASE_DATA = {
    "DZA": { "name": "Algeria", "gdp": "191.9 Billion USD", "system": "Unitary semi-presidential republic" },
    "AGO": { "name": "Angola", "gdp": "106.7 Billion USD", "system": "Unitary presidential republic" },
    "BEN": { "name": "Benin", "gdp": "17.4 Billion USD", "system": "Unitary presidential republic" },
    "BWA": { "name": "Botswana", "gdp": "20.3 Billion USD", "system": "Parliamentary republic" },
    "BFA": { "name": "Burkina Faso", "gdp": "18.8 Billion USD", "system": "Military Junta" },
    "BDI": { "name": "Burundi", "gdp": "3.2 Billion USD", "system": "Presidential republic" },
    "CMR": { "name": "Cameroon", "gdp": "44.3 Billion USD", "system": "Presidential republic" },
    "CAF": { "name": "Central African Rep.", "gdp": "2.5 Billion USD", "system": "Semi-presidential republic" },
    "TCD": { "name": "Chad", "gdp": "11.7 Billion USD", "system": "Transitional Military Council" },
    "COD": { "name": "DR Congo", "gdp": "58.0 Billion USD", "system": "Semi-presidential republic" },
    "COG": { "name": "Rep. of Congo", "gdp": "14.6 Billion USD", "system": "Semi-presidential republic" },
    "CIV": { "name": "Côte d'Ivoire", "gdp": "70.0 Billion USD", "system": "Presidential republic" },
    "DJI": { "name": "Djibouti", "gdp": "3.5 Billion USD", "system": "Presidential republic" },
    "EGY": { "name": "Egypt", "gdp": "476.7 Billion USD", "system": "Semi-presidential republic" },
    "GNQ": { "name": "Eq. Guinea", "gdp": "11.8 Billion USD", "system": "Presidential republic" },
    "ERI": { "name": "Eritrea", "gdp": "2.6 Billion USD", "system": "One-party presidential republic" },
    "ETH": { "name": "Ethiopia", "gdp": "126.8 Billion USD", "system": "Federal parliamentary republic" },
    "GAB": { "name": "Gabon", "gdp": "21.0 Billion USD", "system": "Transitional Military" },
    "GHA": { "name": "Ghana", "gdp": "72.8 Billion USD", "system": "Presidential republic" },
    "GIN": { "name": "Guinea", "gdp": "21.2 Billion USD", "system": "Military Junta" },
    "KEN": { "name": "Kenya", "gdp": "113.4 Billion USD", "system": "Presidential republic" },
    "LBR": { "name": "Liberia", "gdp": "4.0 Billion USD", "system": "Presidential republic" },
    "LBY": { "name": "Libya", "gdp": "45.7 Billion USD", "system": "Provisional Government" },
    "MDG": { "name": "Madagascar", "gdp": "15.0 Billion USD", "system": "Semi-presidential republic" },
    "MLI": { "name": "Mali", "gdp": "18.8 Billion USD", "system": "Military Junta" },
    "MAR": { "name": "Morocco", "gdp": "134.1 Billion USD", "system": "Constitutional monarchy" },
    "MOZ": { "name": "Mozambique", "gdp": "17.8 Billion USD", "system": "Semi-presidential republic" },
    "NAM": { "name": "Namibia", "gdp": "12.6 Billion USD", "system": "Semi-presidential republic" },
    "NER": { "name": "Niger", "gdp": "13.9 Billion USD", "system": "Military Junta" },
    "NGA": { "name": "Nigeria", "gdp": "477.4 Billion USD", "system": "Federal presidential republic" },
    "RWA": { "name": "Rwanda", "gdp": "13.3 Billion USD", "system": "Presidential republic" },
    "SEN": { "name": "Senegal", "gdp": "27.6 Billion USD", "system": "Presidential republic" },
    "SLE": { "name": "Sierra Leone", "gdp": "4.0 Billion USD", "system": "Presidential republic" },
    "SOM": { "name": "Somalia", "gdp": "8.1 Billion USD", "system": "Federal parliamentary republic" },
    "ZAF": { "name": "South Africa", "gdp": "405.9 Billion USD", "system": "Parliamentary republic" },
    "SSD": { "name": "South Sudan", "gdp": "12.0 Billion USD", "system": "Federal transitional republic" },
    "SDN": { "name": "Sudan", "gdp": "51.6 Billion USD", "system": "Military Junta (War)" },
    "TZA": { "name": "Tanzania", "gdp": "75.7 Billion USD", "system": "Presidential republic" },
    "TGO": { "name": "Togo", "gdp": "8.1 Billion USD", "system": "Presidential republic" },
    "TUN": { "name": "Tunisia", "gdp": "46.6 Billion USD", "system": "Presidential republic" },
    "UGA": { "name": "Uganda", "gdp": "45.5 Billion USD", "system": "Presidential republic" },
    "ZMB": { "name": "Zambia", "gdp": "29.7 Billion USD", "system": "Presidential republic" },
    "ZWE": { "name": "Zimbabwe", "gdp": "20.6 Billion USD", "system": "Presidential republic" }
}

# エイリアス辞書
COUNTRY_ALIASES = {
    "Dem. Rep. Congo": "COD", "Democratic Republic of the Congo": "COD",
    "S. Sudan": "SSD", "South Sudan": "SSD",
    "Eq. Guinea": "GNQ", "Equatorial Guinea": "GNQ",
    "Central African Rep.": "CAF", "Central African Republic": "CAF",
    "Côte d'Ivoire": "CIV", "Ivory Coast": "CIV", "Cote d'Ivoire": "CIV",
    "eSwatini": "SWZ", "Swaziland": "SWZ",
    "Rep. of Congo": "COG", "Republic of the Congo": "COG", "Congo": "COG",
    "W. Sahara": "MAR", "Western Sahara": "MAR",
    "Somaliland": "SOM", "Tanzania": "TZA", "United Republic of Tanzania": "TZA"
}

def get_ai_analysis():
    """ChatGPT APIを呼び出して最新の分析を取得"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found.")
        return {}

    client = OpenAI(api_key=api_key)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # プロンプトの作成
    prompt = f"""
    You are a strategic intelligence analyst specializing in African geopolitics.
    Current Date: {today}

    Task:
    Provide a concise risk analysis and stability index for the following countries: {', '.join(TARGET_COUNTRIES)}.
    
    Requirements:
    1. 'risk_analysis': A single, sharp sentence (max 20 words) summarizing the most critical current security or political risk. Be specific (e.g., mention specific rebel groups, economic policies, or recent incidents).
    2. 'stability_index': Choose strictly from [Stable, Moderate, Fragile, Critical].
    
    Output Format:
    Return ONLY a valid JSON object where keys are the 3-letter ISO codes and values are objects containing 'risk_analysis' and 'stability_index'.
    Example: {{ "NGA": {{ "risk_analysis": "Escalating kidnappings in the northwest and inflation spikes.", "stability_index": "Fragile" }} }}
    """

    try:
        print("Contacting ChatGPT for intelligence update...")
        response = client.chat.completions.create(
            model="gpt-4o", # または gpt-3.5-turbo
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return {}

def update_data_file(ai_data):
    """基本データにAIの分析をマージしてファイルに書き出す"""
    merged_data = BASE_DATA.copy()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

    for code, info in BASE_DATA.items():
        if code in ai_data:
            # AIのデータがあれば更新
            ai_info = ai_data[code]
            merged_data[code]["risk_analysis"] = f"[{timestamp}] {ai_info.get('risk_analysis', '')}"
            merged_data[code]["stability_index"] = ai_info.get("stability_index", "Unknown")
        else:
            # なければデフォルト値
            merged_data[code]["risk_analysis"] = merged_data[code].get("risk_analysis", "No recent data.")
            merged_data[code]["stability_index"] = merged_data[code].get("stability_index", "Unknown")

    # JSファイルの内容生成
    js_content = f"""// --- AUTO-GENERATED BY CHATGPT & GITHUB ACTIONS ({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}) ---
const AFRICA_DATA = {json.dumps(merged_data, indent=4)};

const COUNTRY_ALIASES = {json.dumps(COUNTRY_ALIASES, indent=4)};
"""

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Successfully updated data.js with AI insights.")

if __name__ == "__main__":
    ai_results = get_ai_analysis()
    if ai_results:
        update_data_file(ai_results)
    else:
        print("Skipping update due to API failure.")
