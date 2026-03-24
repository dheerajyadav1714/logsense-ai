from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import logsense_agent

app = FastAPI(
    title="LogSense AI",
    description="AI-powered CI/CD log analyzer",
    version="1.0"
)

class LogRequest(BaseModel):
    log: str

@app.get("/")
def home():
    return {"message": "LogSense AI is running 🚀"}

@app.post("/analyze")
async def analyze_log(request: LogRequest):
    try:
        response = logsense_agent.invoke(request.log)

        return {
            "status": "success",
            "data": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
