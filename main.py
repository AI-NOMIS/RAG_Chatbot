from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from query_data import query_rag
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    'https://api.nocodingai.com',
    'https://dev.api.nocodingai.com',
    'https://dev.nocodingai.com',
    'https://pro.nocodingai.com',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class RAGQuery(BaseModel):
#     query_text: str

class RAGResponse(BaseModel):
    response_text: str
    sources: List[str]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/query_rag", response_model=RAGResponse)
def get_rag_data(query_text: str) -> RAGResponse:
    try:
        response_data = query_rag(query_text)
        # Parse the response data into a dictionary
        response_dict = json.loads(response_data)
        return RAGResponse(**response_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
        