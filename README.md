# 🤖 AI Data Analysis Agent

[ai-data-analysis-agent-orecfqss2zfnih82gjprup.streamlit.app](https://ai-data-analysis-agent-orecfqss2zfnih82gjprup.streamlit.app/)

An industry-grade AI-powered Data Analysis Agent built using **FastAPI**, **Pandas**, and **HuggingFace LLMs**.

This system allows users to upload CSV files and automatically generates:

- 📊 Exploratory Data Analysis (EDA)
- ❗ Missing value analysis
- 🧠 AI-generated insights using LLMs
- 📄 Clean, human-readable analytical output (not raw JSON)

---

## 🔍 Project Overview

The AI Data Analysis Agent acts like a junior data analyst that:

- Understands dataset structure
- Performs automated EDA
- Generates human-readable summaries
- Produces AI-driven insights

**Ideal for:**
- Data Science beginners  
- AI/ML Engineers  
- Interview portfolio projects  
- Real-world analytics automation  

---

## 🧱 Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend API | FastAPI |
| Language | Python 3.10+ |
| Data Processing | Pandas |
| AI Model | HuggingFace LLM |
| Server | Uvicorn |
| File Upload | CSV |

---

## 📂 Project Folder Structure

```text
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
```

---

## ⚙️ Features

- 📤 CSV file upload
- 📊 Automatic EDA (rows, columns, missing values)
- 🧠 AI-generated insights (LLM-powered)
- 📄 Clean text output (non-JSON)
- 🧱 Modular agent-based architecture

---

## 🚀 How It Works

1. User uploads a CSV file
2. Dataset is loaded using Pandas
3. `eda_tool` generates dataset summary
4. `insight_agent` calls LLM for insights
5. FastAPI returns a clean analytical response

---

## 🧪 Sample Dataset (Heart Disease)

**Columns:**

- age, sex, cp, trestbps, chol, fbs  
- restecg, thalach, exang, oldpeak  
- slope, ca, thal, target  

---

## 🧠 Example Output

### 📊 Dataset Summary
- Rows: 303  
- Columns: 14  

### ❗ Missing Values
- age: 0  
- sex: 0  
- cp: 0  

### 🧠 AI Insights
- Higher age correlates with increased heart disease risk
- Exercise-induced angina has strong impact
- Cholesterol moderately influences outcomes

---

## 🛠 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/AI-Data-Analysis-Agent.git
cd AI-Data-Analysis-Agent
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

Use **/analyze/** endpoint to upload CSV.

---

## 🧠 Agent Responsibilities

| Agent | Purpose |
|-----|--------|
| intent_agent | Understands user intent |
| planner_agent | Creates analysis plan |
| analysis_agent | Executes analysis |
| insight_agent | Generates AI insights |
| eda_tool | Dataset summary |
| plot_tool | Visualizations |

---

## 📈 Future Enhancements

- 📊 Interactive charts (Streamlit)
- 📄 PDF report generation
- 🧠 RAG-based dataset Q&A
- 🗄 Database support
- 🌐 React frontend

---

## 🎯 Use Cases

- Data analysis automation
- Interview-ready portfolio project
- AI-powered analytics engine
- FastAPI + LLM learning reference

---

## 👨‍💻 Author

**Shubham Raut**  
Data Science & AI Engineer  
Python | ML | LLMs  
Passionate about building intelligent systems
