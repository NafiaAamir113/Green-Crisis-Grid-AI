# 🚀 Green Crisis Grid AI  
### Autonomous Disaster Response & Energy Optimization System

---

## 🧠 Overview

Green Crisis Grid AI is an AI-powered emergency command system that simulates a national-level disaster response center. It combines real-time weather data, Retrieval-Augmented Generation (RAG), hospital prioritization, and intelligent energy allocation to generate structured crisis response plans.

It functions as a digital Emergency Operations Center (EOC) that supports fast, data-driven disaster decision-making.

---

## ⚠️ Problem Statement

During disasters such as floods, heatwaves, and earthquakes, response systems face:

- Delayed decision-making  
- Fragmented data sources  
- Lack of real-time intelligence  
- Inefficient resource allocation  
- No centralized AI command system  

This leads to slower emergency response and increased risk to human lives.

---

## 💡 Solution

Green Crisis Grid AI solves this by building an autonomous crisis intelligence system that:

- Detects disaster severity using real-time weather APIs  
- Retrieves NDMA emergency intelligence using RAG (Pinecone vector database)  
- Prioritizes hospitals based on location  
- Simulates emergency energy redistribution  
- Generates structured government-level reports using LLMs  
- Visualizes crisis zones on an interactive map  

---

## ⚙️ Key Features

- 🌍 Real-time disaster detection (Heatwave, Flood, Fire, Earthquake)  
- 🧠 RAG-based NDMA intelligence retrieval (Pinecone + embeddings)  
- 🏥 Hospital prioritization using distance calculation  
- ⚡ Emergency energy allocation simulation  
- 🤖 AI-generated crisis reports (Together AI - LLaMA 3)  
- 🗺️ Interactive crisis zone mapping (PyDeck)  
- 📊 Automated severity scoring engine  

---

## 🏗️ System Architecture

```mermaid
graph LR
  A[User Input] --> B[Weather/USGS APIs]
  B --> C[Severity Engine]
  C --> D[RAG: Pinecone + NDMA Data]
  D --> E[LLM: Llama 3.3 Reasoning]
  E --> F[Energy/Hospital Optimization]
  F --> G[Interactive Dashboard & Report]

---

## 🧰 Tech Stack

- Streamlit (Frontend UI)
- Python (Core Backend Logic)
- Together AI (LLaMA 3 Model)
- Pinecone (Vector Database for RAG)
- SentenceTransformers (Embeddings)
- Open-Meteo API (Weather Data)
- USGS Earthquake API
- PyDeck (Geospatial Visualization)
- BeautifulSoup (NDMA Data Scraping)

---

## 📊 Output Report Includes

- Risk Level  
- Situation Analysis  
- Immediate Actions  
- Evacuation Plan  
- Hospital Response  
- Government Advisory  
- Executive Summary  

---

## 🚀 Impact

- Faster disaster response decisions  
- AI-powered national emergency simulation  
- Improved resource allocation  
- Real-time crisis visualization  
- Demonstrates future AI governance systems  

---

## 🔗 Live Demo

https://green-crisis-grid-ai-22b2yesnplnehcj3exmraa.streamlit.app/

---

## 📂 Project Structure

- app.py  
- requirements.txt  
- data (NDMA scraped knowledge base)  
- utils  
- README.md  

---

## 👨‍💻 Author

Nafia Aamir  
AI | RAG Systems | Full Stack AI Applications  

---

## 🏁 Conclusion

Green Crisis Grid AI demonstrates how AI can transform disaster management into an autonomous, real-time decision-making system for national-scale emergency response.
