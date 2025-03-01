from fastapi import FastAPI, UploadFile, File, Form
from transcriber import transcribe_audio
from objection_handler import detect_objections
from twilio_handler import initiate_call
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import json

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File to store feedback
FEEDBACK_FILE = "feedback.json"

class CallRequest(BaseModel):
    number: str

@app.post("/transcribe/")
async def transcribe(audio: UploadFile = File(...)):
    """Handles audio transcription"""
    try:
        os.makedirs("temp_audio", exist_ok=True)  
        file_location = f"temp_audio/{audio.filename}"

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        transcription = transcribe_audio(file_location)
        os.remove(file_location)

        return {"transcription": transcription}
    
    except Exception as e:
        return {"error": str(e)}

@app.post("/analyze/")
async def analyze(transcription: str = Form(...)):
    """Analyzes transcription for objections"""
    try:
        objections = detect_objections(transcription)
        return {"objections": objections}

    except Exception as e:
        return {"error": str(e)}

@app.post("/call/")
async def call_customer(request: CallRequest):
    """Initiates a call via Twilio"""
    try:
        call_result = initiate_call(request.number)
        return call_result

    except Exception as e:
        return {"error": str(e)}

@app.post("/submit_feedback/")
async def submit_feedback(
    objection: str = Form(...), 
    selected_response: str = Form(...), 
    agent_notes: str = Form(...)
):
    """Receives and saves agent feedback on AI responses."""
    feedback = {
        "objection": objection,
        "selected_response": selected_response,
        "agent_notes": agent_notes
    }

    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            json.dump([], f)  # Create an empty list

    with open(FEEDBACK_FILE, "r") as f:
        data = json.load(f)

    data.append(feedback)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return {"message": "Feedback submitted successfully"}

@app.get("/call_summary/")
async def call_summary():
    """Generates and returns a summary of objections, agent performance, and AI accuracy."""
    if not os.path.exists(FEEDBACK_FILE):
        return {"error": "No feedback data found"}

    with open(FEEDBACK_FILE, "r") as f:
        data = json.load(f)

    objection_counts = {}
    ai_accuracy = 0
    total_feedback = len(data)

    for feedback in data:
        objection = feedback["objection"]
        objection_counts[objection] = objection_counts.get(objection, 0) + 1

        if feedback["selected_response"]:
            ai_accuracy += 1  

    ai_accuracy = round((ai_accuracy / total_feedback) * 100, 2) if total_feedback else 0

    return {
        "objection_report": objection_counts,
        "ai_accuracy": f"{ai_accuracy}%",
        "total_calls_reviewed": total_feedback
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
