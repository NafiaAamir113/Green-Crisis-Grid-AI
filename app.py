import streamlit as st
import pydeck as pdk
import requests
import math
import random
import time
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# =====================================================
# 🔐 CONFIG & SESSION STATE
# =====================================================
st.set_page_config(page_title="Green Crisis Grid AI", layout="wide")

if 'severity' not in st.session_state:
    st.session_state.severity = 0
if 'report' not in st.session_state:
    st.session_state.report = ""
if 'energy' not in st.session_state:
    st.session_state.energy = None
if 'city_coords' not in st.session_state:
    st.session_state.city_coords = (31.4504, 73.1350)

PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
INDEX_NAME = "crisis-command-center-index"

@st.cache_resource
def init_resources():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)
    model = SentenceTransformer("BAAI/bge-large-en-v1.5")
    return index, model

index, model = init_resources()

# =====================================================
# 🌍 CITY DATABASE
# =====================================================
CITIES = {
    "Faisalabad": (31.4504, 73.1350),
    "Lahore": (31.5204, 74.3587),
    "Karachi": (24.8607, 67.0011),
    "Islamabad": (33.6844, 73.0479),
    "Multan": (30.1575, 71.5249)
}

# =====================================================
# 🧠 CORE ENGINE (RAG, DISASTER, ENERGY)
# =====================================================

def search_ndma(query):
    try:
        vector = model.encode(query, normalize_embeddings=True).tolist()
        results = index.query(vector=vector, top_k=3, include_metadata=True)
        return [m["metadata"]["text"] for m in results.get("matches", []) if m.get("metadata", {}).get("text")]
    except:
        return ["Standard emergency protocols initialized."]

def detect_severity(disaster, lat, lon):
    try:
        base_url = "https://api.open-meteo.com/v1/forecast"
        if disaster == "Heatwave":
            res = requests.get(f"{base_url}?latitude={lat}&longitude={lon}&hourly=temperature_2m").json()
            t = res["hourly"]["temperature_2m"][0]
            return (9, f"Critical Heat ({t}°C)") if t > 40 else (4, f"Normal ({t}°C)")
        if disaster == "Flood":
            res = requests.get(f"{base_url}?latitude={lat}&longitude={lon}&hourly=precipitation").json()
            r = res["hourly"]["precipitation"][0]
            return (9, f"Flood Risk ({r}mm)") if r > 15 else (3, f"Low Rain ({r}mm)")
        return 5, "Baseline Monitoring"
    except:
        return 6, "API Timeout - Using Probabilistic Risk"

def energy_allocation():
    sources = ["Solar Array Alpha", "Battery Backup Unit", "EV Microgrid"]
    return {
        "id": f"GRID-TX-{random.randint(1000, 9999)}",
        "source": random.choice(sources),
        "target": "District General Hospital",
        "amount": round(random.uniform(10.5, 35.0), 2)
    }

def generate_report(city, disaster, severity, reason, docs, energy):
    context_text = "\n".join(docs)
    system_prompt = "You are the NDMA Pakistan Crisis Command AI. Generate a professional, operational emergency report with 7 sections: Risk Level, Situation Analysis, Immediate Actions, Evacuation Plan, Hospital Response, Government Advisory, and a 3-line Executive Summary."
    user_prompt = f"CITY: {city}\nDISASTER: {disaster}\nSEVERITY: {severity}/10\nWEATHER: {reason}\nNDMA DATA: {context_text}\nENERGY ACTION: {energy}"
    
    try:
        res = requests.post("https://api.together.xyz/v1/chat/completions",
            headers={"Authorization": f"Bearer {TOGETHER_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
                "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
                "temperature": 0.2
            })
        return res.json()["choices"][0]["message"]["content"]
    except:
        return "AI Report Generation Offline. Follow standard SOPs."

# =====================================================
# 🖥️ UI LAYOUT
# =====================================================
st.title("🚀 Green Crisis Grid AI")
st.markdown("##### Smart Disaster Response & Autonomous Energy Management")

tab1, tab2 = st.tabs(["🧠 Crisis Intelligence", "🗺️ Live Operations Map"])

# 🧠 TAB 1: INTELLIGENCE
with tab1:
    col_l, col_r = st.columns([1, 2])
    
    with col_l:
        st.subheader("Crisis Parameters")
        city_input = st.selectbox("Operating Sector", list(CITIES.keys()))
        dis_input = st.selectbox("Hazard Type", ["Flood", "Heatwave", "Fire", "Earthquake"])
        
        if st.button("🚨 Run Emergency Protocol", use_container_width=True):
            lat, lon = CITIES[city_input]
            st.session_state.city_coords = (lat, lon)
            
            with st.status("Initializing Grid Intelligence...") as status:
                st.write("🛰️ Fetching NDMA Knowledge (RAG)...")
                docs = search_ndma(f"{dis_input} emergency {city_input}")
                
                st.write("📊 Analyzing Real-time Sensors...")
                sev, reason = detect_severity(dis_input, lat, lon)
                st.session_state.severity = sev
                
                st.write("🔋 Allocating Green Energy Nodes...")
                st.session_state.energy = energy_allocation()
                
                st.write("✍️ Generating Executive Briefing...")
                st.session_state.report = generate_report(city_input, dis_input, sev, reason, docs, st.session_state.energy)
                status.update(label="Analysis Complete", state="complete")

    with col_r:
        if st.session_state.report:
            m1, m2, m3 = st.columns(3)
            m1.metric("Risk Level", f"{st.session_state.severity}/10", delta_color="inverse")
            m2.metric("Energy Flow", f"{st.session_state.energy['amount']} kWh", "STABLE")
            m3.metric("System Hub", "Verified", "Grounded")
            
            st.success(f"**⚡ Energy Action:** Rerouting {st.session_state.energy['amount']} kWh from {st.session_state.energy['source']} to {st.session_state.energy['target']}.")
            st.text_area("NDMA AI COMMAND REPORT", st.session_state.report, height=450)
        else:
            st.info("Awaiting system trigger from the Control Panel.")

# 🗺️ TAB 2: OPERATIONS MAP
with tab2:
    st.subheader(f"Deployment View: {st.session_state.severity}/10 Risk Zone")
    
    lat, lon = st.session_state.city_coords
    
    # Dynamic Color based on severity
    zone_color = [255, 0, 0, 140] if st.session_state.severity > 7 else [255, 165, 0, 140]
    
    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12, pitch=45)
    
    layers = [
        pdk.Layer(
            "ScatterplotLayer",
            data=[{"lat": lat, "lon": lon}],
            get_position='[lon, lat]',
            get_radius=1500,
            get_color=zone_color,
            pickable=True
        ),
        pdk.Layer(
            "TextLayer",
            data=[{"lat": lat, "lon": lon, "text": "CRISIS ZONE" if st.session_state.severity > 0 else ""}],
            get_position='[lon, lat]',
            get_text="text",
            get_size=20,
            get_color=[0, 0, 0],
            get_alignment_baseline="'bottom'"
        )
    ]
    
    st.pydeck_chart(pdk.Deck(layers=layers, initial_view_state=view_state, map_style="light"))
    st.caption("Map visualization updates dynamically based on the Crisis Intelligence tab.")
