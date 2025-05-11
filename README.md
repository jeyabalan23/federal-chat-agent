

## Overview
A simple RAG-based chatbot that fetches, cleans, and loads federal data into MySQL and enables chat queries using LLM.

## Setup
1. Clone the repo.
2. Set MySQL credentials in `.env`.
3. Run `pip install -r requirements.txt`
4. Launch with `uvicorn api.main:app --reload`

## Folder Structure
- `data_pipeline/`: Data download and preprocessing.
- `database/`: SQL schema.
- `agent/`: Core RAG logic.
- `api/`: FastAPI endpoint.
- `ui/`: Basic HTML frontend.
- `utils/`: Async fetchers.

## Usage
Visit `localhost:8000` and use the chat UI.

---

Let me know if you want this exported as a downloadable `.zip` next.


