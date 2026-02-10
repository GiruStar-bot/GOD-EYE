// --- MANUAL UPDATE BY GEMINI (2026-02-11) ---
// Latest geopolitical intelligence and risk analysis.

const AFRICA_DATA = {
    "DZA": {
        "name": "Algeria",
        "gdp": "205.0 Billion USD",
        "system": "Unitary semi-presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Upcoming elections stir debate; continued reliance on hydrocarbon revenues amidst global energy shifts."
    },
    "AGO": {
        "name": "Angola",
        "gdp": "110.5 Billion USD",
        "system": "Unitary presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Public dissatisfaction with high living costs persists despite oil output stabilization."
    },
    "BEN": {
        "name": "Benin",
        "gdp": "19.2 Billion USD",
        "system": "Unitary presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Security forces engaging jihadist groups spilling over from northern border with Burkina Faso."
    },
    "BWA": {
        "name": "Botswana",
        "gdp": "21.5 Billion USD",
        "system": "Parliamentary republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Economic diversification efforts continue; stable political environment post-2024 elections."
    },
    "BFA": {
        "name": "Burkina Faso",
        "gdp": "20.1 Billion USD",
        "system": "Military Junta",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Jihadist groups control significant territory; humanitarian crisis worsening in blockaded towns."
    },
    "BDI": {
        "name": "Burundi",
        "gdp": "3.8 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Tension with Rwanda over rebel support allegations; economic isolation challenges."
    },
    "CMR": {
        "name": "Cameroon",
        "gdp": "48.2 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Succession uncertainty for long-standing leadership; Anglophone separatist conflict persists."
    },
    "CAF": {
        "name": "Central African Rep.",
        "gdp": "2.7 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Heavy reliance on mercenary groups for security; rebel control in rural areas remains high."
    },
    "TCD": {
        "name": "Chad",
        "gdp": "12.5 Billion USD",
        "system": "Transitional Military Council",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Refugee influx from Sudan straining resources; delayed transition to civilian rule sparks protests."
    },
    "COD": {
        "name": "DR Congo",
        "gdp": "65.0 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] M23 rebels threatening Goma; widespread displacement in North Kivu amidst regional diplomatic standoff."
    },
    "COG": {
        "name": "Rep. of Congo",
        "gdp": "15.8 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Concerns over long-term debt sustainability and oil price volatility."
    },
    "CIV": {
        "name": "Côte d'Ivoire",
        "gdp": "78.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Strong economic growth; military reinforcing northern border against Sahelian threat."
    },
    "DJI": {
        "name": "Djibouti",
        "gdp": "3.9 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Strategic stability maintained despite regional turbulence in Red Sea and Ethiopia-Somalia tension."
    },
    "EGY": {
        "name": "Egypt",
        "gdp": "490.0 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Inflation easing slightly; focus on border security due to Gaza and Sudan conflicts."
    },
    "GNQ": {
        "name": "Eq. Guinea",
        "gdp": "11.5 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Oil production decline posing fiscal risks; tight political control continues."
    },
    "ERI": {
        "name": "Eritrea",
        "gdp": "2.8 Billion USD",
        "system": "One-party presidential republic",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Highly militarized society; international isolation; potential involvement in Sudan conflict."
    },
    "ETH": {
        "name": "Ethiopia",
        "gdp": "135.0 Billion USD",
        "system": "Federal parliamentary republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Post-war reconstruction in Tigray; persistent insurgencies in Amhara and Oromia regions."
    },
    "GAB": {
        "name": "Gabon",
        "gdp": "22.5 Billion USD",
        "system": "Transitional Military",
        "stability_index": "Uncertain",
        "risk_analysis": "[2026-02] Transition timetable under scrutiny; emphasis on diversifying economy from oil."
    },
    "GHA": {
        "name": "Ghana",
        "gdp": "76.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Debt restructuring progress aiding recovery; preparing for upcoming competitive elections."
    },
    "GIN": {
        "name": "Guinea",
        "gdp": "23.0 Billion USD",
        "system": "Military Junta",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Simandou iron ore project developing; slow progress on return to civilian rule."
    },
    "KEN": {
        "name": "Kenya",
        "gdp": "120.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Economic reforms stabilizing currency; police deployed to Haiti returning; regional diplomacy active."
    },
    "LBR": {
        "name": "Liberia",
        "gdp": "4.3 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Infrastructure challenges; focus on anti-corruption measures by administration."
    },
    "LBY": {
        "name": "Libya",
        "gdp": "48.0 Billion USD",
        "system": "Provisional Government",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Political stalemate between East and West administrations; sporadic clashes in Tripoli."
    },
    "MDG": {
        "name": "Madagascar",
        "gdp": "16.0 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Cyclonic season recovery; political protests regarding recent electoral reforms."
    },
    "MLI": {
        "name": "Mali",
        "gdp": "19.5 Billion USD",
        "system": "Military Junta",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] JNIM blockade impacting Bamako; withdrawal from ECOWAS finalized; security situation dire."
    },
    "MAR": {
        "name": "Morocco",
        "gdp": "145.0 Billion USD",
        "system": "Constitutional monarchy",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Earthquake reconstruction advanced; growing diplomatic recognition of Western Sahara claims."
    },
    "MOZ": {
        "name": "Mozambique",
        "gdp": "19.0 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Cabo Delgado insurgency contained but not eliminated; LNG projects resuming slowly."
    },
    "NAM": {
        "name": "Namibia",
        "gdp": "13.5 Billion USD",
        "system": "Semi-presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Smooth political transition following recent elections; green hydrogen projects advancing."
    },
    "NER": {
        "name": "Niger",
        "gdp": "15.0 Billion USD",
        "system": "Military Junta",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Oil export challenges due to Benin border tensions; high threat from ISGS and JNIM."
    },
    "NGA": {
        "name": "Nigeria",
        "gdp": "490.0 Billion USD",
        "system": "Federal presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Economic outlook revised to positive due to reforms; kidnapping and banditry in northwest remain acute."
    },
    "RWA": {
        "name": "Rwanda",
        "gdp": "14.5 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] High diplomatic tension with DRC over M23 allegations; domestic politics remain tightly controlled."
    },
    "SEN": {
        "name": "Senegal",
        "gdp": "30.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] New administration's anti-corruption drive sparking parliamentary debate; oil production boosting growth."
    },
    "SLE": {
        "name": "Sierra Leone",
        "gdp": "4.2 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] High inflation provoking sporadic social unrest; political dialogue attempting to ease tensions."
    },
    "SOM": {
        "name": "Somalia",
        "gdp": "9.0 Billion USD",
        "system": "Federal parliamentary republic",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Constitutional changes disputed; Al-Shabaab resilient in central regions; Ethiopia tension lingering."
    },
    "ZAF": {
        "name": "South Africa",
        "gdp": "410.0 Billion USD",
        "system": "Parliamentary republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Coalition government testing stability; focus on solving energy and logistics crises."
    },
    "SSD": {
        "name": "South Sudan",
        "gdp": "12.5 Billion USD",
        "system": "Federal transitional republic",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] Oil pipeline disruptions affecting revenue; inter-communal violence high ahead of delayed elections."
    },
    "SDN": {
        "name": "Sudan",
        "gdp": "40.0 Billion USD",
        "system": "Military Junta (War)",
        "stability_index": "Critical",
        "risk_analysis": "[2026-02] RSF advancing in Kordofan; catastrophic famine in Darfur; peace talks stalled."
    },
    "TZA": {
        "name": "Tanzania",
        "gdp": "82.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Infrastructure projects driving growth; political reconciliation process continuing."
    },
    "TGO": {
        "name": "Togo",
        "gdp": "9.2 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Constitutional changes to parliamentary system causing opposition protests; northern border security tight."
    },
    "TUN": {
        "name": "Tunisia",
        "gdp": "48.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Migration crisis straining resources; economic stagnation and debt repayment risks."
    },
    "UGA": {
        "name": "Uganda",
        "gdp": "49.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Moderate",
        "risk_analysis": "[2026-02] Preparing for 2026 elections; ADF attacks in west persist but contained."
    },
    "ZMB": {
        "name": "Zambia",
        "gdp": "31.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Stable",
        "risk_analysis": "[2026-02] Debt restructuring finalized; copper production recovery focus; drought impact management."
    },
    "ZWE": {
        "name": "Zimbabwe",
        "gdp": "22.0 Billion USD",
        "system": "Presidential republic",
        "stability_index": "Fragile",
        "risk_analysis": "[2026-02] Currency volatility remains; crackdown on dissent continues post-election."
    }
};

const COUNTRY_ALIASES = {
    "Dem. Rep. Congo": "COD", "Democratic Republic of the Congo": "COD",
    "S. Sudan": "SSD", "South Sudan": "SSD",
    "Eq. Guinea": "GNQ", "Equatorial Guinea": "GNQ",
    "Central African Rep.": "CAF", "Central African Republic": "CAF",
    "Côte d'Ivoire": "CIV", "Ivory Coast": "CIV", "Cote d'Ivoire": "CIV",
    "eSwatini": "SWZ", "Swaziland": "SWZ",
    "Rep. of Congo": "COG", "Republic of the Congo": "COG", "Congo": "COG",
    "W. Sahara": "MAR", "Western Sahara": "MAR",
    "Somaliland": "SOM", "Tanzania": "TZA", "United Republic of Tanzania": "TZA"
};
