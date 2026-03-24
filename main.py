from fastapi import FastAPI
from pydantic import BaseModel
from agent import logsense_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.models import Content, Part   # ✅ Correct import

app = FastAPI()

session_service = InMemorySessionService()
runner = Runner(
    app_name="logsense_app",
    agent=logsense_agent,
    session_service=session_service
)

class LogRequest(BaseModel):
    log: str

@app.get("/")
def home():
    return {"message": "LogSense AI running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/analyze")
async def analyze_log(request: LogRequest):
    try:
        content = Content(parts=[Part(text=request.log)])

        events = []
        for event in runner.run(
            user_id="user",
            session_id="session",
            input=content
        ):
            events.append(event)

        if events:
            last_event = events[-1]
            if last_event.content and last_event.content.parts:
                analysis = last_event.content.parts[0].text
            else:
                analysis = "No response content"
        else:
            analysis = "No events returned"

        return {
            "status": "success",
            "analysis": analysis
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
