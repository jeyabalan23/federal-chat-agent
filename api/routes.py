# Route definitions for the FastAPI app
from fastapi import APIRouter
from agent.agent import run_agent

router = APIRouter()

@router.post("/ask")
def ask_question(question: str):
    return {"response": run_agent(question)}

