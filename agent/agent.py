# Code for the LLM agent logic
from agent.tools import summarize_text
from agent.llm_interface import query_llm

def run_agent(input_text):
    summary = summarize_text(input_text)
    return query_llm(summary)

