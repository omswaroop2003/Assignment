from transformers import pipeline
import json 
import os

# Load NLP model for objection handling
nlp_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# List of common objections in sales calls
COMMON_OBJECTIONS = [
    "We don’t have the budget",
    "We use another provider",
    "Not interested",
    "Call me later"
]
FEEDBACK_FILE = "feedback_data.json"

def save_feedback(agent_feedback):
    """Saves AI feedback from the agent to a JSON file."""
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            json.dump([], f)

    with open(FEEDBACK_FILE, "r") as f:
        data = json.load(f)

    data.append(agent_feedback)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return {"message": "Feedback saved successfully"}


def detect_objections(text, threshold=0.6):
    """Detects objections in a given conversation text."""
    if not text.strip():
        return {"error": "Empty input text"}

    try:
        results = nlp_model(text, COMMON_OBJECTIONS)  # Compare text against objections

        # Filter objections that exceed the threshold
        objections_detected = [
            {"objection": label, "confidence": round(score, 2)}
            for label, score in zip(results["labels"], results["scores"])
            if score > threshold
        ]

        return {"objections": objections_detected}

    except Exception as e:
        return {"error": str(e)}
