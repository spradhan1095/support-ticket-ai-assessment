# AI-Powered Support Ticket Analytics System

## Overview

This project is an AI-powered Support Ticket Analytics System built using FastAPI, Streamlit, Pandas, and Groq Llama 3.1. The system enables users to analyze support ticket data, detect anomalies, visualize operational metrics, and ask natural language questions about ticket performance.

The solution combines Large Language Models (LLMs) for intent understanding with deterministic analytics using Pandas to ensure accurate and reliable results.

---

## Features

### Dashboard Analytics

* Total Tickets
* Open Tickets
* Resolved Tickets
* Escalated Tickets
* Average Customer Rating
* Ticket Status Distribution
* Priority Distribution
* Agent Performance Analysis

### Natural Language Querying

Users can ask questions such as:

* How many open tickets are there?
* Which support engineer is performing best?
* What is the average customer rating?
* Which category has the most tickets?
* How many escalated tickets exist?

The system uses a Groq-hosted Llama 3.1 model to identify user intent and then performs the required analytics using Pandas.

### Anomaly Detection

The system automatically identifies:

* Tickets with unusually long resolution times
* Critical unresolved tickets
* Poor customer ratings
* Slow response times

---

## Technology Stack

### Backend

* FastAPI
* Python
* Pandas
* NumPy
* Pydantic
* Groq API

### Frontend

* Streamlit
* Plotly

### AI / LLM

* Groq Llama 3.1

---

## Project Structure

```text
support_ticket_ai/
│
├── backend/
│   ├── api/
│   │   ├── health.py
│   │   ├── query.py
│   │   ├── dashboard.py
│   │   └── anomaly.py
│   │
│   ├── services/
│   │   ├── data_loader.py
│   │   ├── analytics_service.py
│   │   ├── anomaly_detector.py
│   │   ├── llm_service.py
│   │   └── query_engine.py
│   │
│   ├── schemas/
│   │   └── schemas.py
│   │
│   ├── data/
│   │   └── support_tickets.csv
│   │
│   ├── config.py
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## Architecture

```text
Support Ticket CSV
        │
        ▼
   Data Loader
        │
        ▼
 Pandas DataFrame
        │
 ┌──────┼──────────┐
 │      │          │
 ▼      ▼          ▼
Analytics  Query Engine  Anomaly Detector
              │
              ▼
          Groq LLM
     (Intent Detection)
              │
              ▼
      Structured Intent
              │
              ▼
       Pandas Analysis
              │
              ▼
          FastAPI APIs
              │
              ▼
        Streamlit UI
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Dashboard Metrics

```http
GET /dashboard
```

Returns dashboard KPIs.

---

### Query Endpoint

```http
POST /query
```

Request:

```json
{
  "question": "Who is the best support engineer?"
}
```

Response:

```json
{
  "answer": "AGT-05 has the highest average rating of 4.8."
}
```

---

### Anomaly Detection

```http
GET /anomalies
```

Returns detected anomalies.

---

## Anomaly Detection Logic

### Rule 1: Long Resolution Time

Tickets with:

```text
Resolution Time > Mean + 2 × Standard Deviation
```

are flagged as anomalies.

### Rule 2: Critical Unresolved Tickets

```text
Priority = Critical
AND
Status ≠ Resolved
```

### Rule 3: Poor Customer Rating

```text
Customer Rating ≤ 2
```

### Rule 4: Slow Response Time

```text
Response Time > 24 Hours
```

---

## LLM Integration

The project uses Groq Llama 3.1 for intent detection.

Example:

User Question:

```text
Who is the best support engineer?
```

LLM Intent:

```text
highest_rated_agent
```

The Query Engine then executes the corresponding Pandas operation and returns the result.

This hybrid architecture combines:

* Natural Language Understanding (LLM)
* Deterministic Analytics (Pandas)

to ensure both flexibility and accuracy.

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd support_ticket_ai
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

---

## Running the Backend

Navigate to backend directory:

```bash
cd backend
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Running the Frontend

Open a new terminal:

```bash
cd frontend
```

Start Streamlit:

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Future Enhancements

* PostgreSQL Integration
* Redis Caching
* Role-Based Authentication
* Semantic Search with Vector Databases
* Retrieval-Augmented Generation (RAG)
* Machine Learning-Based Anomaly Detection
* NL-to-SQL Query Generation
* Agentic AI Workflows

---

## Trade-Offs

### CSV vs Database

CSV was selected for simplicity and rapid development given the small dataset size. PostgreSQL would be preferred for large-scale production workloads.

### Rule-Based Anomaly Detection

Rule-based detection provides explainability and simplicity. Machine learning methods could improve detection of complex anomaly patterns.

### Streamlit vs React

Streamlit enabled rapid dashboard development while allowing focus on AI and backend functionality.

---

## Author

Sushant Kumar Pradhan

AI Engineer Assessment Submission
