# Starter code for FastAPI REST API assignment

# main.py
# 1. Install FastAPI and Uvicorn before running:
#    pip install fastapi uvicorn
# 2. Run the server:
#    uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add your CRUD endpoints and models below
