This project is a **real-time call objection handling system** that integrates:
- ✅ **LiveKit** for live call streaming.
- ✅ **Twilio** for call initiation.
- ✅ **Hugging Face API** for transcription & objection analysis.
- ✅ **MERN stack** (MongoDB, Express.js, React.js, Node.js).
Tech Stack
Frontend:React.js,LiveKit SDK
Backend:FastAPI (Python),Twilio API,Hugging Face AI,Whisper ASR
---

## 🚀 **1. Setup Guide**

### 🖥 **Backend Setup**
2️⃣ Backend Setup (FastAPI)
Install Dependencies
cd backend
pip install fastapi[all]

Create .env File in backend/
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone
HUGGING_FACE_API_KEY=your_huggingface_key

Run FastAPI Server
uvicorn main:app --reload
FastAPI runs at http://127.0.0.1:8000.
1️⃣ **Navigate to frontend directory**  
cd frontend

2️⃣Install dependencies
npm install

3️⃣ Set up .env file
Create a .env file inside backend/ and add:
REACT_APP_LIVEKIT_SERVER=wss://your-livekit-url
REACT_APP_API_BASE_URL=http://localhost:8000
 Run Server
npm start
  
Postman Sample Testing 
API Testing (Postman Collection)
1️⃣ Initiate Call
Endpoint: POST /call/
Request Body (JSON):
{
    "number": "+917032290722"
}
Response:
{
    "message": "Call initiated successfully",
    "call_sid": "CAxxxxxxxxxxxxxxxxx"
}
2️⃣ Transcribe Audio
Endpoint: POST /transcribe/
Response:
{
    "transcription": "Hello, how can I help you today?"
}
3️⃣ Submit Feedback
Endpoint: POST /submit_feedback/
Request Body (Form Data):
objection=Pricing issue
selected_response=We offer discounts for bulk purchases
agent_notes=Customer needed discount details
Response:
{
    "message": "Feedback submitted successfully"
}
4️⃣ Get Call Summary
Endpoint: GET /call_summary/
Response:
{
    "objection_report": {"Pricing issue": 2, "Service issue": 1},
    "ai_accuracy": "90%",
    "total_calls_reviewed": 10
}
Screenshots provided below
![Screenshot (587)](https://github.com/user-attachments/assets/969a12cd-bafd-49c3-b505-317da52479a8)
![Screenshot (586)](https://github.com/user-attachments/assets/d971d4be-8f4c-4981-afef-8e2acaaa432a)
![Screenshot (585)](https://github.com/user-attachments/assets/78733efd-8833-42f1-b4d1-6357dc24310a)

Common Issues & Solutions
1)Twilio Call Error 422->	Trial account, unverified number ->	Use a verified number wth same country code of active number or upgrade
2)LiveKit not loading->	Invalid API key	-> Check .env file
3)Transcription not working -> Hugging Face API issue	-> Ensure correct API key

All the testing are done through postman and screenshots are provided and as OpenAi is paid version i have used Huggingface pre trained ai model 
u can go through the files

Thank you
