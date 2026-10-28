
from fastapi import FastAPI
from datetime import datetime, timezone
import platform

app = FastAPI(
    title="DevOps Control Center API",
    description="Backend para monitoramento DevOps",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "project": "DevOps Control Center",
        "status": "online",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/system")
def system_info():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "python": platform.python_version()
    }
