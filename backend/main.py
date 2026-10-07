from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from simulator import get_state, set_pose

app = FastAPI(title="AirPulse+ Prototype API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE = Path(__file__).resolve().parent.parent
INDEX = BASE / "frontend" / "index.html"

@app.get("/api/vitals")
def vitals():
    return get_state()

@app.post("/api/pose/{pose}")
def pose(pose: str):
    return set_pose(pose)

@app.get("/")
def home():
    return FileResponse(INDEX)

@app.get("/{path:path}")
def frontend(path: str):
    target = BASE / "frontend" / path
    if target.is_file():
        return FileResponse(target)
    return FileResponse(INDEX)
