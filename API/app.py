import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

''' 
 INSTRUCTIONS TO RUN THE FASTAPI APP:
     
    # 1. Install FastAPI and Uvicorn if you haven't already:
    pip install fastapi uvicorn
    
    #2. Create a virtual environment and activate it: 
    python -m venv venv
    
    #3. Move to the directory where the app.py file is located and run the command below in the terminal:
    > cd API
    
    #4. To run the FastAPI app, use the command below in the terminal:
    uvicorn app:app --reload
 
    #5. Open google chrome and go to url:  http://127.0.0.1:8000/familia
 
 '''