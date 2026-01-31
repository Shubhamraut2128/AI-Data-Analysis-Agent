🤖 AI Data Analysis Agent

An industry-grade AI-powered Data Analysis Agent built using FastAPI, Pandas, and HuggingFace LLMs.
This project allows users to upload CSV datasets and automatically generates:
---
📊 Exploratory Data Analysis (EDA)

❗ Missing value analysis

🧠 AI-generated insights using LLMs

🚀 Clean, readable (non-JSON) analytical output

🔍 Project Overview

The AI Data Analysis Agent acts like a junior data analyst that:

Understands the dataset structure

Performs quick EDA

Generates human-readable summaries

Produces AI-driven insights

This project is designed for:

Data Science beginners

AI/ML Engineers

Interview demos

Real-world analytics automation

🧱 Tech Stack
Layer	Technology
Backend API	FastAPI
Language	Python 3.10+
Data Processing	Pandas
AI Model	HuggingFace LLM
API Server	Uvicorn
File Upload	CSV
📂 Project Folder Structure
AI_DATA_ANALYSIS_AGENT/
│
├── agents/
│   ├── __init__.py
│   ├── analysis_agent.py
│   ├── hf_llm.py
│   ├── insight_agent.py
│   ├── intent_agent.py
│   └── planner_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── data_cleaner.py
│   ├── data_loader.py
│   ├── eda_tool.py
│   └── plot_tool.py
│
├── data/
│   └── uploads/
│       └── loan.csv
│
├── app.py
├── main.py
├── requirements.txt
└── README.md

⚙️ Features

📤 Upload CSV file

📊 Automatic EDA (rows, columns, missing values)

🧠 AI-generated insights (LLM-powered)

📄 Clean text output (not raw JSON)

🏗 Modular agent-based architecture

🚀 How It Works

User uploads a CSV file

Dataset is loaded using Pandas

eda_tool generates dataset summary

insight_agent calls LLM to generate insights

FastAPI returns a clean, readable analysis

🧪 Sample Dataset (Heart Disease)

Example columns:

age, sex, cp, trestbps, chol, fbs, restecg,
thalach, exang, oldpeak, slope, ca, thal, target

🧠 Example Output
📊 Dataset Summary
Rows: 303
Columns: 14

🧾 Column Names:
- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal
- target

❗ Missing Values:
- age: 0
- sex: 0
- cp: 0
...

🧠 AI Insights:
- Higher age correlates with increased heart disease risk
- Exercise-induced angina shows strong impact
- Cholesterol levels moderately influence outcomes

🛠 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/AI-Data-Analysis-Agent.git
cd AI-Data-Analysis-Agent

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
uvicorn main:app --reload


Open browser:

http://127.0.0.1:8000/docs


Use /analyze/ endpoint to upload CSV.

🔗 API Endpoint
POST /analyze/

Input:

CSV file upload

Output:

Dataset summary

Missing values

AI-generated insights (text format)

🧠 Agent Responsibilities
Agent	Purpose
intent_agent	Understands user intent
planner_agent	Creates analysis plan
analysis_agent	Executes analysis
insight_agent	Generates AI insights
eda_tool	Dataset summary
plot_tool	Visualizations (optional)
📈 Future Enhancements

📊 Interactive charts (Streamlit)

📄 PDF report generation

🧠 RAG-based dataset Q&A

🗄 Database support

🌐 React frontend

🎯 Use Cases

Data analysis automation

Interview portfolio project

AI-powered analytics tool

Learning FastAPI + LLM integration

👨‍💻 Author

Shubham Raut

Data Science & AI Engineer

Java | Python | ML | LLMs

Passionate about building intelligent systems
