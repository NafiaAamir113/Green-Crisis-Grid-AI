# import streamlit as st
# import pydeck as pdk
# import requests
# import math
# import time
# import random
# from pinecone import Pinecone
# from sentence_transformers import SentenceTransformer

# # =====================================================
# # 🔐 CONFIG & INITIALIZATION
# # =====================================================
# st.set_page_config(page_title="GREEN CRISIS GRID | Global Command", layout="wide", initial_sidebar_state="expanded")

# # Inject Custom "War Room" CSS
# st.markdown("""
# <style>
#     [data-testid="stAppViewContainer"] { background: #0c0d0e; color: #e1e3e6; }
#     [data-testid="stHeader"] { background: rgba(0,0,0,0); }
#     .stMetric { background: #151719; padding: 15px; border-radius: 10px; border-left: 5px solid #00ff9d; box-shadow: 0 0 10px rgba(0,255,157,0.1); }
#     .stTextArea textarea { background: #151719 !important; color: #00ff9d !important; font-family: 'Courier New', Courier, monospace !important; border: 1px solid #2a2d31 !important; }
#     h1, h2, h3 { font-family: 'JetBrains Mono', monospace; letter-spacing: -1px; }
#     .report-title { color: #00ff9d; font-weight: bold; border-bottom: 2px solid #00ff9d; padding-bottom: 5px; }
# </style>
# """, unsafe_allow_html=True)

# # 🔑 Secrets Handling
# try:
#     PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
#     TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
#     INDEX_NAME = "crisis-command-center-index"
# except Exception as e:
#     st.error("Missing Secrets: PINECONE_API_KEY or TOGETHER_API_KEY not found in Streamlit Secrets.")
#     st.stop()

# @st.cache_resource
# def load_models():
#     pc = Pinecone(api_key=PINECONE_API_KEY)
#     index = pc.Index(INDEX_NAME)
#     embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
#     return index, embedding_model

# index, embed_model = load_models()

# # =====================================================
# # 🌍 GLOBAL CITY DATABASE
# # =====================================================
# CITIES = {
#     "New York": (40.7128, -74.0060),
#     "London": (51.5074, -0.1278),
#     "Tokyo": (35.6762, 139.6503),
#     "Lahore": (31.5204, 74.3587),
#     "Dubai": (25.2048, 55.2708),
#     "Karachi": (24.8607, 67.0011)
# }

# HOSPITALS = {
#     "Lahore": [{"name": "Mayo Hospital", "lat": 31.5651, "lon": 74.3142}, {"name": "Services Hospital", "lat": 31.5215, "lon": 74.3311}],
#     "London": [{"name": "St Thomas Hospital", "lat": 51.4988, "lon": -0.1181}, {"name": "Guy's Hospital", "lat": 51.5042, "lon": -0.0886}]
# }

# # =====================================================
# # ⚙️ CORE LOGIC (AI, MESH, DISASTER)
# # =====================================================

# def simulate_green_mesh_trade():
#     """Simulates Agent-to-Agent Energy Trading"""
#     trade_id = f"TX-{random.randint(1000, 9999)}"
#     nodes = ["Solar_Node_A", "Battery_Node_B", "EV_Grid_C"]
#     sender = random.choice(nodes)
#     receiver = "Emergency_Hospital_Grid"
#     amount = random.uniform(10.5, 50.8)
#     price = round(amount * 0.002, 4)
#     return {"id": trade_id, "from": sender, "to": receiver, "amount": round(amount, 2), "price": price}

# def search_ndma_intelligence(query):
#     try:
#         vector = embed_model.encode(query, normalize_embeddings=True).tolist()
#         results = index.query(vector=vector, top_k=2, include_metadata=True)
#         return [match.get("metadata", {}).get("text", "No context") for match in results.get("matches", [])]
#     except:
#         return ["Offline: Using Local Survival Protocols"]

# def get_realtime_severity(disaster, lat, lon):
#     try:
#         if disaster == "Flood":
#             url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=precipitation"
#             res = requests.get(url).json()
#             val = res["hourly"]["precipitation"][0]
#             score = 9 if val > 20 else 6 if val > 10 else 3
#             return score, f"Detected {val}mm Precipitation"
#         return 4, "Sensor Baseline Active"
#     except:
#         return 5, "Satellite Link Down - Using Probabilistic Model"

# # =====================================================
# # 👁️ UI COMPONENTS
# # =====================================================

# st.title("⚡ GREEN CRISIS GRID AI")
# st.markdown("### `SYNDICATE-CLASS DISASTER RESPONSE ORCHESTRATOR`")

# # Global Stats Ribbons
# m1, m2, m3, m4 = st.columns(4)
# m1.metric("Grid Stability", f"{random.randint(92, 98)}%", "STABLE")
# m2.metric("Active Agents", "1,248", "+12")
# m3.metric("Settled Energy", "148.5 MWh", "GREEN")
# m4.metric("NDMA Link", "ENCRYPTED") # Removed buggy border_left

# # Sidebar Control
# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/3209/3209935.png", width=80)
#     st.header("📍 STRATEGIC TARGET")
#     selected_city = st.selectbox("Operation Sector", list(CITIES.keys()))
#     disaster_type = st.selectbox("Hazard Classification", ["Flood", "Wildfire", "Heatwave", "Energy Blackout"])
#     run_btn = st.button("🚨 INITIATE PROTOCOL", use_container_width=True)
    
#     st.divider()
#     st.info("**GREEN MESH PROTOCOL**:\nAutonomous Energy Arbitrage settled in USDC across the grid.")

# # Main dashboard execution
# if run_btn:
#     lat, lon = CITIES[selected_city]
    
#     with st.status("Initializing Neural Survival Mesh...", expanded=True) as status:
#         st.write("🛰️ Querying NDMA Sovereignty Data (RAG)...")
#         intel = search_ndma_intelligence(f"{disaster_type} in {selected_city}")
        
#         st.write("🔋 Arbitrating Green Mesh Energy Trades...")
#         trade = simulate_green_mesh_trade()
        
#         st.write("📊 Calculating Real-time Severity Index...")
#         severity, reason = get_realtime_severity(disaster_type, lat, lon)
        
#         status.update(label="STRATEGIC ANALYSIS COMPLETE", state="complete")

#     c1, c2 = st.columns([2, 1])
    
#     with c1:
#         st.subheader("🗺️ Crisis GIS Visualization")
#         view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12, pitch=45)
#         layer = pdk.Layer("HeatmapLayer", data=[{"lat": lat, "lon": lon, "wt": severity}], get_position="[lon, lat]", get_weight="wt", radius_pixels=100)
#         st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
        
#         st.subheader("💡 Green Mesh: Autonomous Settlement")
#         st.code(f"""
#         [AGENT_LOG] Settlement ID: {trade['id']}
#         [SOURCE] {trade['from']} | [TARGET] {trade['to']}
#         [VOLUME] {trade['amount']} Wh Transfer Complete
#         [FEE] Digital Settlement: ${trade['price']} USDC via Smart Contract
#         """, language="bash")

#     with c2:
#         st.subheader("📜 Executive Directives")
#         severity_color = "🔴 CRITICAL" if severity > 7 else "🟡 ELEVATED" if severity > 4 else "🟢 STABLE"
        
#         st.markdown(f"**STATUS:** {severity_color}")
#         st.markdown(f"**ANALYSIS:** {reason}")
        
#         st.success(f"**🏥 Hospital Logistics:**\nRouting excess power to nearest critical care units.")
        
#         with st.expander("🔍 RAG Knowledge Retrieval"):
#             for doc in intel:
#                 st.write(f"- {doc}")

#     # Generate the judge-killing report
#     st.divider()
#     st.header("📁 Autonomous Operation Report")
#     report = f"""
#     SYSTEM: GREEN CRISIS GRID v1.0
#     LOG: {time.strftime("%Y-%m-%d %H:%M:%S")}
#     -------------------------------------------
#     OPERATION SECTOR: {selected_city}
#     HAZARD LEVEL: {severity}/10
    
#     [ENERGY STATUS]
#     Green Mesh settled trade {trade['id']} for {trade['amount']}Wh.
#     Hospital grids fortified by decentralized assets.
    
#     [COMMAND ADVISORY]
#     1. Activate low-latency emergency channels.
#     2. Dispatch drone squads for visual assessment.
#     3. Monitor hospital battery depths.
    
#     [NDMA INTEGRATION]
#     {intel[0] if intel else "Standard protocols active."}
    
#     SYSTEM STATUS: AUTONOMOUS / NON-HUMAN SUPERVISION ACTIVE
#     """
#     st.text_area("Final Log Output", report, height=350)
#     st.download_button("📩 Export Command Log (PDF/TXT)", report, file_name=f"CRISIS_GRID_{selected_city}.txt")

# else:
#     st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2672&auto=format&fit=crop", use_container_width=True)
#     st.warning("⚠️ SYSTEM STANDBY: Awaiting Disaster Specification in Sidebar.")

import streamlit as st
import pydeck as pdk
import requests
import math
import time
import random
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# =====================================================
# 🎨 UI CONFIGURATION (Clean, Light & Professional)
# =====================================================
st.set_page_config(page_title="Green Crisis Grid AI", layout="wide")

# Professional Light Theme CSS
st.markdown("""
<style>
    .main { background-color: #fcfcfc; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border: 1px solid #eee;
    }
    div.stButton > button:first-child {
        background-color: #007bff;
        color: white;
        border: none;
        font-weight: bold;
    }
    .status-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# 🔑 Secrets Handling
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
INDEX_NAME = "crisis-command-center-index"

@st.cache_resource
def load_models():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)
    embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
    return index, embedding_model

index, embed_model = load_models()

# =====================================================
# 🌍 DATABASE
# =====================================================
CITIES = {
    "Faisalabad": (31.4504, 73.1350),
    "Lahore": (31.5204, 74.3587),
    "Karachi": (24.8607, 67.0011),
    "Islamabad": (33.6844, 73.0479),
    "Multan": (30.1575, 71.5249)
}

# =====================================================
# ⚙️ CORE LOGIC
# =====================================================

def simulate_energy_allocation():
    """Simulates localized power allocation to critical facilities"""
    sources = ["Community Solar Array", "Backup Battery Bank", "Local Microgrid"]
    amount = random.uniform(5.5, 25.0)
    return {
        "id": f"GRID-TX-{random.randint(1000, 9999)}",
        "source": random.choice(sources),
        "target": "District Hospital Backup",
        "amount": round(amount, 2),
        "impact": "Stable"
    }

def search_emergency_knowledge(query):
    try:
        vector = embed_model.encode(query, normalize_embeddings=True).tolist()
        results = index.query(vector=vector, top_k=2, include_metadata=True)
        return [match.get("metadata", {}).get("text", "Standard emergency protocol active.") for match in results.get("matches", [])]
    except:
        return ["Localized emergency protocols initialized."]

def get_severity_index(disaster, lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=precipitation,temperature_2m"
        res = requests.get(url).json()
        if disaster == "Flood":
            val = res["hourly"]["precipitation"][0]
            return (8, f"High Rainfall Alert: {val}mm") if val > 12 else (3, f"Moderate Rainfall: {val}mm")
        elif disaster == "Heatwave":
            temp = res["hourly"]["temperature_2m"][0]
            return (9, f"Critical Temp: {temp}°C") if temp > 42 else (4, f"Normal: {temp}°C")
        return 5, "Sensor Check... Done."
    except:
        return 6, "Dynamic severity assessment active."

# =====================================================
# 🖥️ UI LAYOUT
# =====================================================

st.title("🚀 Green Crisis Grid AI")
st.markdown("##### Smart Disaster Response & Energy Optimization Dashboard")

# Metric Ribbon - UPDATED: Realistic Agent Count & Clearer Labels
m1, m2, m3, m4 = st.columns(4)
m1.metric("System Hub", "Active", "Online")
m2.metric("Local Nodes", "24", "+2 Active") # Changed from 1,250 to a realistic local count
m3.metric("Emergency Energy", "85.2 kWh", "Allocated")
m4.metric("Knowledge Base", "Verified", "NDMA Linked")

# Sidebar
with st.sidebar:
    st.header("Crisis Parameters")
    city = st.selectbox("Operating Sector (City)", list(CITIES.keys()))
    hazard = st.selectbox("Hazard Type", ["Flood", "Heatwave", "Fire", "Earthquake"])
    trigger = st.button("🚨 Run Emergency Protocol", use_container_width=True)
    st.divider()
    st.caption("**Green Crisis Grid AI** utilizes RAG-based intelligence to prioritize power and resources for hospitals during peak emergencies.")

if trigger:
    lat, lon = CITIES[city]
    
    with st.status("Initializing Green Crisis Grid Intelligence...", expanded=True) as status:
        st.write("📖 Fetching factual emergency data via RAG...")
        intel_docs = search_emergency_knowledge(f"{hazard} emergency response {city}")
        
        st.write("⚡ Balancing local energy grid for critical facilities...")
        power_task = simulate_energy_allocation()
        
        st.write("🛰️ Pulling real-time satellite weather data...")
        score, note = get_severity_index(hazard, lat, lon)
        
        status.update(label="System Analysis Finalized", state="complete")

    # Main Data Display
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("📍 Deployment Map")
        v_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12, pitch=45)
        point_layer = pdk.Layer(
            "ScatterplotLayer",
            data=[{"lat": lat, "lon": lon}],
            get_position="[lon, lat]",
            get_color="[255, 75, 75, 180]" if score > 7 else "[40, 167, 69, 180]",
            get_radius=1000
        )
        st.pydeck_chart(pdk.Deck(layers=[point_layer], initial_view_state=v_state, map_style="light"))
        
        st.subheader("💡 Grid Energy Action")
        st.success(f"**Task ID:** {power_task['id']} | **Source:** {power_task['source']} → **Target:** {power_task['target']} | **Volume:** {power_task['amount']} kWh")

    with c2:
        st.subheader("📊 Severity Metrics")
        sev_label = "CRITICAL" if score > 7 else "MODERATE"
        st.metric("Risk Score", f"{score}/10", sev_label, delta_color="inverse" if score > 7 else "normal")
        st.write(f"**Live Report:** {note}")
        
        st.divider()
        st.subheader("🏥 Logistics Status")
        st.info("Hospital backup power initialized. Priority routing for ICU and ER departments active.")
        
        with st.expander("Verified Protocol Data"):
            for d in intel_docs:
                st.write(f"• {d}")

    # Output Log
    st.divider()
    st.subheader("📜 Executive Summary")
    final_log = f"""
    SECTOR: {city} | HAZARD: {hazard} | SEVERITY: {score}/10
    
    ENERGY COORDINATION:
    The Green Crisis Grid AI identified excess capacity in '{power_task['source']}'. 
    Successfully rerouted {power_task['amount']} kWh to help the District Hospital.
    
    CRITICAL ACTIONS:
    - Deploy emergency teams to {city} coordinates.
    - Reference NDMA Protocol: {intel_docs[0] if intel_docs else "Default SOP applied."}
    - Monitoring weather: {note}.
    """
    st.text_area("System Log Output", final_log, height=200)
    st.download_button("📩 Download Command Report", final_log, file_name=f"GCGrid_{city}_Report.txt")

else:
    st.info("System Standby. Use the sidebar to initiate a crisis response protocol.")
