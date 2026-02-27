# 🚢 Titanic Dataset Chat Agent

The **Titanic Dataset Chat Agent** is an intelligent, conversational AI application that lets you explore the famous Titanic passenger dataset through natural language — no code required. Ask questions in plain English, and the agent responds with real-time statistics, computed insights, and dynamic visualizations. Whether you're a data enthusiast, a student, or a developer exploring AI-powered data tools, this project demonstrates how modern LLM-based agents can make data analysis intuitive and interactive.


## 🔍 Project Overview

This project combines a **FastAPI** backend with a **Streamlit** frontend to create a seamless chat interface for querying the Titanic dataset. Under the hood, a **LangChain agent** powered by **Groq (Llama 3.3 70B)** interprets your questions, runs the appropriate data operations on the dataset, and returns both textual answers and visual charts.

### ✨ Key Features

- **Natural Language Queries** — Ask questions like *"What percentage of 1st class passengers survived?"* or *"What was the average ticket fare?"*
- **Dynamic Statistics** — Computes mean, count, median, percentages, and more — with optional filters
- **Data Visualizations** — Generates histograms and graphs for deeper data insights
- **Chat-style UI** — Clean, user-friendly Streamlit interface for a smooth conversational experience
- **REST API Backend** — FastAPI backend with full API documentation available at `/docs`


## 🎥 Project Demo Link

> 🔗 **Live Demo:** https://titanic-chat-agent1.streamlit.app/

> 📸 **Screenshot:** <img width="1915" height="977" alt="image" src="https://github.com/user-attachments/assets/8757584d-1a34-412b-9b36-5fc5e3aa5958" />


## 📁 Project Structure

```
titanic-dataset-chat-agent/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── backend/
│   ├── main.py
│   └── services/
│       ├── agent.py
│       └── prompts.py
├── data/
│   ├── Titanic-Dataset.csv
│   └── titanic_cleaned.csv
├── frontend/
│   └── app.py
└── notebooks/
    ├── building_agent.ipynb
    └── checking_data.ipynb
```


## 🛠️ Tech Stack Used

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit |
| **Backend** | FastAPI + Uvicorn |
| **AI / LLM** | Llama 3.3 70B (via `langchain_groq`) |
| **Agent Framework** | LangChain |
| **Data Processing** | Pandas |
| **Visualizations** | Matplotlib|
| **Data Validation** | Pydantic |
| **Dataset** | Titanic Passenger Dataset (CSV) |
| **Language** | Python 3.11 |


## ⚙️ Project Setup

Follow the steps below to run the project locally on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Sayan-Mondal2022/titanic-dataset-chat-agent.git
cd titanic-dataset-chat-agent
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Open `backend.py` and replace the placeholder with your actual **Groq API key**:

```python
# In backend.py
GROQ_API_KEY = "YOUR_API_KEY"
```

> 💡 You can obtain a free API key from [Groq](https://console.groq.com/home).

### 5. Start the FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

The backend will be running at:
- **Base URL:** `http://127.0.0.1:8000`
- **API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`

### 6. Start the Streamlit Frontend

Open a **new terminal** (with your virtual environment activated) and run:

```bash
streamlit run app.py
```

The Streamlit interface will automatically open in your default browser. You can now start chatting with the Titanic dataset!


## 🙏 Acknowledgement

A heartfelt thank you to the following tools, frameworks, and communities that made this project possible:

- [**LangChain**](https://www.langchain.com/) — for the powerful agent and tool-use framework
- [**Groq**](https://console.groq.com/home) — for providing the large language model powering the chat agent
- [**FastAPI**](https://fastapi.tiangolo.com/) — for the blazing-fast and developer-friendly API framework
- [**Streamlit**](https://streamlit.io/) — for making it easy to build beautiful data apps
- [**Pandas**](https://pandas.pydata.org/) — for robust data manipulation and analysis
- [**Matplotlib**](https://matplotlib.org/) & [**Seaborn**](https://seaborn.pydata.org/) — for data visualization
- [**Kaggle**](https://www.kaggle.com/c/titanic) — for the classic Titanic dataset


## 🤝 Thank You

Thank you for visiting this repository! 🌟

If you found this project helpful or interesting, please consider giving it a ⭐ on GitHub — it means a lot and motivates further development.

Feel free to **fork**, **contribute**, or **raise issues** if you find any bugs or have suggestions for improvement. Contributions of all kinds are welcome!

> Made with ❤️ by [Sayan Mondal](https://github.com/Sayan-Mondal2022)

---

*Happy exploring! 🚀*
