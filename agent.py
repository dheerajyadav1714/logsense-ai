from google.adk.agents import LlmAgent
import vertexai

vertexai.init(
    project="gcp-experiments-490315",
    location="asia-south1"
)

root_agent = LlmAgent(   # <-- renamed from logsense_agent
    name="logsense_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a DevOps expert.
    Analyze the provided log and return:
    - Root cause
    - Suggested fix
    - Severity (low/medium/high)
    Format your answer clearly.
    """
)
