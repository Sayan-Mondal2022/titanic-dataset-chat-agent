from backend.services.prompts import prompt
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent

df = pd.read_csv("data/titanic_cleaned.csv")

load_dotenv()

# USING GROQ
model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )

agent = create_pandas_dataframe_agent(
        llm=model,
        df=df,
        allow_dangerous_code=True,
        prefix=prompt
    )

def run_agent(query: str):
    response = agent.invoke(query)
    return response["output"]