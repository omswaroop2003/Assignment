import os
from transformers import pipeline

# Load Whisper model
whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

from fastapi import Form

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
    
    save_feedback(feedback)
    
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

        # AI accuracy is assumed to be based on whether the agent used the suggested response
        if feedback["selected_response"]:
            ai_accuracy += 1  

    ai_accuracy = round((ai_accuracy / total_feedback) * 100, 2) if total_feedback else 0

    return {
        "objection_report": objection_counts,
        "ai_accuracy": f"{ai_accuracy}%",
        "total_calls_reviewed": total_feedback
    }

def transcribe_audio(audio_path):
    """Transcribes an audio file using Whisper."""
    if not os.path.exists(audio_path):
        return {"error": "Audio file not found"}

    try:
        result = whisper_model(audio_path)  # Process audio
        return result["text"]
    except Exception as e:
        return {"error": str(e)}
