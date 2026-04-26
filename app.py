import streamlit as st
import pydeck as pdk
import requests
import math
import time
import random
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# =====================================================
# 🔐 SYSTEM CONFIG & SECRETS
# =====================================================
st.set_page_config(page_title="GREEN CRISIS GRID | Global Command", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for the "Command Center" Aesthetic
st.markdown("""
<style>
    .reportview-container { background: #0e1117; }
    .stMetric { background: #1a1c23; padding: 15px; border-radius: 10px; border-left: 5px solid #00ff9d; }
    .stTextArea textarea { font-family: 'Courier New', Courier, monospace; background-color: #000; color: #00ff9d; }
    .status-active { color: #00ff9d; font-weight: bold; animation: blink 1s infinite; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
</style>
""", unsafe_allow_html=True)

PINECONE_API_KEY = st.secrets.get("PINECONE_API_KEY", "")
TOGETHER_API_KEY = st.secrets.get("TOGETHER_API_KEY", "")
INDEX_NAME = "crisis-command-center-index"

# Initialize AI & DB (Cached for speed)
@st.cache_resource
def init_systems():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)
    model = SentenceTransformer("BAAI/bge-large-en-v1.5")
    return index, model

# =====================================================
# 🌍 GLOBAL DATASETS
# =====================================================
CITIES = {
    "Lahore": (31.5204, 74.3587),
    "Karachi": (24.8607, 67.0011),
    "Islamabad": (33.6844, 73.0479),
    "Multan": (30.1575, 71.5249),
    "Faisalabad": (31.4504, 73.1350)
}

HOSPITALS = {
    "Lahore": [
        {"name": "Mayo Hospital", "lat": 31.5651, "lon": 74.3142},
        {"name": "Jinnah Hospital", "lat": 31.4697, "lon": 74.2867},
        {"name": "Services Hospital", "lat": 31.5215, "lon": 74.3311},
    ],
    "Karachi": [
        {"name": "JPMC", "lat": 24.8600, "lon": 67.0100},
        {"name": "Civil Hospital", "lat": 24.8550, "lon": 67.0300},
        {"name": "Aga Khan Hospital", "lat": 24.8937, "lon": 67.0686},
    ],
}

# =====================================================
# ⚡ THE "GREEN MESH" (AGENT-TO-AGENT TRADING)
# =====================================================
def run_green_mesh_simulation(severity):
    """Simulates multi-agent energy trading when grid stability is compromised"""
    st.markdown("### ⚡ Green Mesh: Active Agent Trading")
    
    agents = ["Solar_Node_Alpha", "Battery_Unit_B7", "EV_Grid_S1", "Hospital_Backup_Gen"]
    trades = []
    
    cols = st.columns(len(agents))
    for i, agent in enumerate(agents):
        usage = random.randint(40, 95) if severity > 5 else random.randint(10, 40)
        cols[i].metric(agent, f"{usage}% Load", f"{'- High' if usage > 80 else 'Steady'}")
    
    # Simulate Transactions
    if severity > 4:
        for _ in range(3):
            seller = random.choice(agents[:2])
            buyer = random.choice(agents[2:])
            amount = random.randint(50, 200)
            price = round(amount * 0.0024, 4)
            trades.append(f"TRANSACTION SETTLED: {seller} -> {buyer} | {amount}Wh @ ${price} USDC")
            
    return trades

# =====================================================
# 📡 NDMA DATA INTEGRATION (Simulation of live retrieval)
# =====================================================
def get_ndma_intel():
    """Retrieves high-level strategy from NDMA data source or PDF index"""
    # Note: For the hackathon, simulate fetching the LATEST NDMA bulletin
    bulletins = [
        "NDMA Bulletin #42: Flood risk in Punjab low-lying areas. Level 2 Alert.",
        "NDMA Strategic Note: Thermal clusters detected in Southern Karachi. Activate cooling centers.",
        "NDMA/PDMA Alert: Seismic tremors expected in North. Verify Hospital Backup Grids."
    ]
    return random.choice(bulletins)

# =====================================================
# 🧠 CORE LOGIC & AI
# =====================================================
def search_pinecone(query, index, model):
    try:
        vector = model.encode(query, normalize_embeddings=True).tolist()
        results = index.query(vector=vector, top_k=3, include_metadata=True)
        return [match.get("metadata", {}).get("text") for match in results.get("matches", []) if match.get("metadata", {}).get("text")]
    except: return ["Manual backup: Activate standard disaster protocols."]

def get_weather_data(lat, lon, feature):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly={feature}"
        res = requests.get(url).json()
        val = res["hourly"][feature][0]
        return val
    except: return 0

# =====================================================
# 🎨 UI LAYOUT
# =====================================================
st.sidebar.markdown("# 🛡️ SYSTEM UPLINK")
selected_city = st.sidebar.selectbox("COMMAND TARGET (City)", list(CITIES.keys()))
disaster_type = st.sidebar.selectbox("DISASTER VECTOR", ["Flood", "Heatwave", "Earthquake", "Wildfire"])
run_btn = st.sidebar.button("SYNC & DEPLOY SYSTEM", use_container_width=True)

# Metric Dashboard
m1, m2, m3, m4 = st.columns(4)
m1.metric("System Latency", "14ms", "Real-time")
m2.metric("Active Nodes", "1,242", "+14")
m3.metric("Grid Stability", "94%", "-2%")
m4.metric("NDMA Status", "Connected", border_left=True)

if run_btn:
    index, model = init_systems()
    lat, lon = CITIES[selected_city]
    
    with st.status("Initializing Green Crisis Mesh...", expanded=True) as status:
        st.write("🛰️ Connecting to Satellite Uplink...")
        # Get real data
        rain = get_weather_data(lat, lon, "precipitation")
        temp = get_weather_data(lat, lon, "temperature_2m")
        
        # Severity Logic
        severity = 3
        if disaster_type == "Flood" and rain > 10: severity = 8
        elif disaster_type == "Heatwave" and temp > 40: severity = 9
        
        st.write("📊 Analyzing Grid Vulnerability...")
        time.sleep(1)
        st.write("🤖 Running Agent-to-Agent Negotiations...")
        trades = run_green_mesh_simulation(severity)
        status.update(label="System Desynchronization Prevented. Response Active.", state="complete")

    # GIS Map Section
    st.markdown("### 🗺️ Dynamic Crisis Map (GIS)")
    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=11, pitch=50)
    
    # Layer for hospitals
    h_data = HOSPITALS.get(selected_city, [])
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=view_state,
        layers=[
            pdk.Layer("HeatmapLayer", [{"lat": lat, "lon": lon, "w": severity}], get_position='[lon, lat]', get_weight='w', radiusPixels=100),
            pdk.Layer("ScatterplotLayer", h_data, get_position='[lon, lat]', get_color='[0, 255, 157]', get_radius=5000),
        ]
    ))

    # Knowledge Base + Output
    st.markdown("### 📋 AI Strategic Report & Neural Logs")
    colA, colB = st.columns([1, 1])
    
    with colA:
        st.markdown("#### Strategic Strategy")
        intel = get_ndma_intel()
        st.info(f"**LATEST NDMA INTEL:** {intel}")
        
        # Here you would call generate_ai_report from your code
        st.code(f"""
        TARGET: {selected_city}
        THREAT: {disaster_type}
        SEVERITY: {severity}/10
        EVACUATION: {'REQUIRED' if severity > 7 else 'MONITORING'}
        """, language="yaml")
        
    with colB:
        st.markdown("#### Green Mesh Ledger")
        for trade in trades:
            st.success(trade)
        if not trades:
            st.write("No grid arbitrage required. Load is stable.")

else:
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=2072", use_container_width=True)
    st.info("Awaiting System Synchronization. Select Target City in the Sidebar.")
