# LogSense AI – DevOps Log Analysis Agent

LogSense AI is an intelligent DevOps assistant that automates CI/CD log analysis. It uses Google ADK and Gemini 2.5 Flash to transform raw logs into a clear summary, root cause, and actionable fix suggestions.

## 🚀 Features

- ✅ Automated log summarization  
- ✅ Root cause identification  
- ✅ Actionable fix suggestions  
- ✅ Simple HTTP API (`POST /run`)  
- ✅ ADK Web UI for interactive testing  
- ✅ Serverless scaling via Cloud Run  

## 🛠️ Tech Stack

- **Language:** Python 3.11  
- **AI Framework:** Google ADK  
- **Model:** Gemini 2.5 Flash  
- **Cloud:** Google Cloud Run  
- **Container:** Docker (managed by ADK CLI)

## 📦 Project Structure
.
├── agent.py # ADK agent definition (root_agent)
├── .env # (optional) environment variables
├── .gitignore
└── README.md

text

## 🔧 Setup (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/dheerajyadav1714/logsense-ai.git
   cd logsense-ai
Install dependencies

bash
pip install google-adk google-cloud-aiplatform python-dotenv
Set up environment variables
Create a .env file with:

text
PROJECT_ID=your-gcp-project-id
LOCATION=asia-south1
MODEL=gemini-2.5-flash
Run the ADK web server locally

bash
adk web .
Then open http://localhost:8000 in your browser.

☁️ Deployment to Cloud Run
Use the ADK CLI to deploy (ensure you are authenticated with gcloud):

bash
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=asia-south1 \
  --service_name=logsense-api \
  --with_ui \
  . \
  -- \
  --allow-unauthenticated
After deployment, you'll get a URL like https://logsense-api-xxxxxx-uc.a.run.app.

📡 API Usage
Endpoint: POST /run

Request body (JSON):

json
{
  "appName": "logsense_ai",
  "userId": "user",
  "sessionId": "your-unique-session-id",
  "newMessage": {
    "role": "user",
    "parts": [{"text": "ERROR: Connection timeout to database after 30s"}]
  },
  "stateDelta": null,
  "streaming": false
}
Response:
A JSON array of events. The final event contains the analysis in content.parts[0].text.

Example curl (creates a new session automatically):

bash
SESSION_ID=$(python -c "import uuid; print(uuid.uuid4())")
curl -X POST https://logsense-api-xxx.asia-south1.run.app/run \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "logsense_ai",
    "userId": "user",
    "sessionId": "'"$SESSION_ID"'",
    "newMessage": {
      "role": "user",
      "parts": [{"text": "ERROR: Connection timeout to database after 30s"}]
    },
    "stateDelta": null,
    "streaming": false
  }'
🖥️ Web UI
You can also interact with the agent via the ADK Web UI at:
https://logsense-api-xxx.asia-south1.run.app/dev-ui/?app=logsense_ai

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/050f9b70-0812-4217-819e-b375168b86e8" />


🧠 AI Prompt Design
The core intelligence is driven by a specialized prompt:

text
You are a Senior DevOps Engineer.

Analyze CI/CD pipeline logs and provide:

- Summary:
- Root Cause:
- Fix Suggestion:
- Severity:

Focus on:
- Exact failure point
- Clear root cause
- Practical fixes

Avoid:
- Generic explanations
- Irrelevant details
  
📝 License
This project is for demonstration purposes as part of the Gen AI Academy submission.

