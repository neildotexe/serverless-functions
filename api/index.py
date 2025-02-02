from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware 
import json

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

with open("api/q-vercel-python.json", "r") as f:
    marks_list = json.load(f)

student_data = {mark["name"]: mark["marks"] for mark in marks_list}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    result = [student_data.get(n, None) for n in name]
    return {"marks": result}