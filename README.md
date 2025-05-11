# Chat RAG Agent

## Overview
An agent-based system powered by a local LLM that retrieves and reasons over US federal register data.

## Features
- Data pipeline to fetch and load federal register documents.
- MySQL backend.
- Local LLM (Ollama) with tool use.
- FastAPI + minimal HTML UI.

## Setup
1. Clone repo
2. Create `.env` file (example included)
3. Run MySQL and setup schema from `database/schema.sql`
4. Run `python data_pipeline/fetch_federal_data.py`
5. Start FastAPI: `uvicorn api.main:app --reload`

## Notes
- Make sure Ollama is running locally.
- Use `qwen:1b` or similar small models.
