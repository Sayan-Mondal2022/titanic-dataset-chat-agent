from backend.services.agent import run_agent
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow frontend connection (important for Streamlit later) FOR LOCAL SETUP
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:8501"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],
#     allow_headers=["Authorization", "Content-Type"],
# )

# For deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(query: QueryRequest):
    try:
        # Delete old plot before running so we can detect fresh ones
        if os.path.exists("output.png"):
            os.remove("output.png")

        response = run_agent(query.question)

        return {
            "success": True,
            "answer": response,
            "has_plot": os.path.exists("output.png")  # True only if agent just saved one
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.get("/plot")
def get_plot():
    if os.path.exists("output.png"):
        return FileResponse("output.png", media_type="image/png")
    return {"error": "No plot generated yet."}