from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_context
from gemma import ask_gemma




app = FastAPI()

class Query(BaseModel):
    message: str


@app.post("/chat")

def chat(query: Query):
    
    context = get_context(query.message)
     # create a system prompt for the model 
    prompt = f"""
    You are a flood safety AI for Bangladesh.

    Context:
    {context}

    User:
    {query.message}

    Give short, clear advice in Bangla or simple English.
    """

    response = ask_gemma(prompt)
    return {"response": response}