# AI-Powered Support Ticket Analytics System

## Overview

This project is an AI-powered Support Ticket Analytics System built using FastAPI, Streamlit, Pandas, and Python. The application enables users to analyze support ticket data, detect anomalies, and interact with the dataset using natural language queries.

The system processes a CSV dataset containing support tickets and provides insights through APIs and an interactive dashboard.

---

## Features

### Natural Language Querying

Users can ask questions in plain English such as:

* How many open tickets are there?
* How many resolved tickets are there?
* Which category has the most tickets?
* Which agent has the highest rating?
* What is the average customer rating?
* What is the average response time?

The query engine interprets user intent and performs data analysis directly on the dataset to return accurate responses.

---

### Anomaly Detection

The system identifies potential operational issues using predefined business rules:

#### Long Resolution Time

Tickets with unusually high resolution times compared to the dataset average.

#### Critical Unresolved Tickets

Critical priority tickets that have not been resolved.

#### Poor Customer Ratings

Tickets with customer ratings less than or equal to 2.

#### Slow Response Time

Tickets with response times greater than 24 hours.

---

### Dashboard Analytics

The Streamlit dashboard provides:

* Total Tickets
* Open Tickets
* Resolved Tickets
* Escalated Tickets
* Average Customer Rating

Visualizations include:

* Ticket Status Distribution
* Priority Distribution
* Agent Performance Analysis

---

## Project Architecture

```text
Support Ticket CSV
        │
        ▼
Data Loader (Pandas)
        │
        ▼
Query Engine
        │
        ├────────► Analytics Service
        │
        ├────────► Anomaly Detector
        │
        ▼
FastAPI Backend
        │
        ▼
Streamlit Frontend
```

---

## Folder Structure

```text
support-ticket-ai/
│
├── backend/
│   ├── api/
│   │   ├── health.py
│   │   ├── query.py
│   │   ├── anomaly.py
│   │   └── dashboard.py
│   │
│   ├── services/
│   │   ├── data_loader.py
│   │   ├── query_engine.py
│   │   ├── anomaly_detector.py
│   │   ├── analytics_service.py
│   │   └── llm_service.py
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
├── tests/
│
├── requirements.txt
├── .env
└── README.md
```

---

## Technologies Used

### Backend

* FastAPI
* Python
* Pandas
* NumPy
* Pydantic

### Frontend

* Streamlit
* Plotly

### AI Components

* Rule-Based Query Engine
* Natural Language Processing Logic

### Data Processing

* Pandas DataFrames
* Statistical Analysis

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

### Dashboard Summary

```http
GET /dashboard
```

Returns:

```json
{
  "total_tickets": 500,
  "open_tickets": 111,
  "resolved_tickets": 295,
  "escalated_tickets": 94,
  "avg_rating": 3.45
}
```

---

### Anomaly Detection

```http
GET /anomalies
```

Returns detected anomalies and anomaly count.

---

### Natural Language Query

```http
POST /query
```

Request:

```json
{
  "question": "How many open tickets are there?"
}
```

Response:

```json
{
  "answer": "There are 111 open tickets."
}
```

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd support-ticket-ai
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

---

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Navigate to backend folder:

```bash
cd backend
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Open a new terminal:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Sample Questions

The system can answer:

* How many total tickets are there?
* How many open tickets are there?
* How many resolved tickets are there?
* How many escalated tickets are there?
* How many critical tickets are there?
* How many unresolved critical tickets are there?
* Which category has the most tickets?
* Which agent has the highest rating?
* Which agent has the lowest rating?
* What is the average customer rating?
* What is the average response time?
* What is the average resolution time?

---

## Design Decisions

### Why FastAPI?

FastAPI provides high performance, automatic API documentation, data validation, and a clean architecture for backend services.

### Why Streamlit?

Streamlit allows rapid development of data-centric dashboards and analytics applications with minimal frontend complexity.

### Why a Rule-Based Query Engine?

Instead of relying solely on an LLM, the system performs calculations directly on the dataset using Pandas. This ensures:

* Accurate results
* No hallucinations
* Better explainability
* Deterministic outputs

---

## Future Enhancements

* PostgreSQL integration
* LangChain-based AI Agents
* Role-Based Access Control
* Docker Deployment
* Cloud Deployment (AWS/Azure/GCP)
* Real-time ticket ingestion
* Advanced Machine Learning-based anomaly detection
* Vector Database integration for semantic search

---

## Author

Sushant Kumar Pradhan

AI Engineer Assessment Submission
