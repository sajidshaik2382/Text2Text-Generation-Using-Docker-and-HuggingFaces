from fastapi import FastAPI
from transformers import pipeline

# create a new Fast API APP instance

app = FastAPI()
# initialize the text generation pipeline


pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
def home():
    return {"meaasge":"hello World"}

# define a function to handle the Get request at '/generate'


@app.get("/generate")
def generate(text:str):

    output=pipe(text)

    return {"output":output[0]['generated_text']}
