# 🚀 Green Crisis Grid AI  
### Autonomous Disaster Response & Energy Optimization System

---

## 🧠 Overview

**Green Crisis Grid AI** is an AI-powered emergency command system that simulates a national-level disaster response center. It combines real-time weather data, **Retrieval-Augmented Generation (RAG)**, hospital prioritization, and intelligent energy allocation to generate structured crisis response plans.

It functions as a digital **Emergency Operations Center (EOC)** that supports fast, data-driven disaster decision-making.

---

## ⚠️ Problem Statement

During disasters such as floods, heatwaves, and earthquakes, response systems face:

- **Delayed decision-making** due to information overload.
- **Fragmented data sources** across different agencies.
- **Lack of real-time intelligence** for immediate field action.
- **Inefficient resource allocation** (specifically energy grids).
- **No centralized AI command system** to bridge the gap.

This leads to slower emergency response and increased risk to human lives.

---

## 💡 Solution

Green Crisis Grid AI solves this by building an autonomous crisis intelligence system that:

- **Detects disaster severity** using real-time weather APIs.
- **Retrieves NDMA emergency intelligence** using RAG (Pinecone vector database).
- **Prioritizes hospitals** based on location and real-time energy needs.
- **Simulates emergency energy redistribution** from green sources.
- **Generates structured government-level reports** using Meta-Llama 3.3.
- **Visualizes crisis zones** on an interactive PyDeck map.

---

## ⚙️ Key Features

- 🌍 **Real-time Detection:** Automated monitoring for Heatwaves, Floods, Fire, and Earthquakes.
- 🧠 **RAG Intelligence:** Context-aware retrieval using Pinecone + `bge-large` embeddings.
- 🏥 **Medical Prioritization:** Logic-based hospital routing and status monitoring.
- ⚡ **Energy Mesh:** Autonomous solar/battery energy redistribution simulation.
- 🤖 **AI-Generated Directives:** Professional briefings powered by Llama 3.3.
- 🗺️ **Interactive GIS:** Real-time crisis zone mapping and spatial visualization.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[User Input] --> B{External APIs}
    B -->|Weather/Seismic| C[Severity Engine]
    C --> D[RAG: Pinecone + NDMA Data]
    D --> E[LLM: Llama 3.3 Reasoning]
    E --> F[Energy & Hospital Optimization]
    F --> G[Interactive Dashboard & Report]



    style A fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#00ff9d,stroke:#333,stroke-width:2px
    style D fill:#D6EAF8,stroke:#333,stroke-width:1px
```
---

### 🧰 Tech Stack
* **Frontend:** Streamlit (Clean, professional UI)
* **Reasoning Engine:** Meta-Llama 3.3-70B via Together AI (Chosen for superior instruction-following in high-stakes reporting)
* **Vector Database:** Pinecone Serverless (RAG implementation)
* **Embeddings:** `BAAI/bge-large-en-v1.5` (State-of-the-art retrieval accuracy)
* **Geospatial:** PyDeck (Interactive GIS) & Open-Meteo API
* **Data Ingestion:** BeautifulSoup (Used for scraping and structuring NDMA knowledge bases)

---

### 📊 Tactical Report Output
The AI generates a structured "Executive Directive" including:
1. **Risk Level:** A normalized severity index.
2. **Situation Analysis:** Real-time environmental breakdown.
3. **Immediate Actions:** Priority-1 tactical maneuvers for first responders.
4. **Evacuation Plan:** Geographic-specific routing advice.
5. **Hospital Response:** Power status and distance-based triage logistics.
6. **Government Advisory:** Prepared official public-facing communication.
7. **Executive Summary:** A concise 3-line briefing for rapid decision-making.

---

### 🚀 Impact & Future Scope
* **Reduced Response Time:** Moves from manual data gathering to AI-generated briefs in seconds.
* **AI Governance:** Demonstrates how RAG can be used to keep AI systems legally and operationally grounded.
* **Future Work:** Integration of LangGraph for multi-agent negotiation and live IoT sensors for microgrid management.

---

### 🏁 Conclusion
Green Crisis Grid AI demonstrates how autonomous systems can bridge the gap between "Big Data" and "Rapid Action," ensuring that during a national crisis, the grid stays stable and lives are saved through AI-driven precision.

---

### 👨‍💻 Author
**Nafia Aamir**
*AI Researcher | RAG Systems Specialist*
