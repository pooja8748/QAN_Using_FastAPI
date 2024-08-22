from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import gunicorn
import uvicorn
from roberta import nlp_qna 

app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],                      
     )

@app.get("/answers/{contex}/{question}")
def answer(contex,question):
    result = nlp_qna(contex, question)

    if not result:
        raise HTTPException(status_code=400)
    return result
