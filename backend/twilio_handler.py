from twilio.rest import Client

TWILIO_SID = "AC85997bdb56c56717dc60792c8d22ca8e"
TWILIO_AUTH = "f461976f3d3c3f9c12f37c289e39ce12"
TWILIO_PHONE = "+13174589622"

client = Client(TWILIO_SID, TWILIO_AUTH)

def initiate_call(phone_number):
    """Initiates a Twilio call to a given phone number."""
    if not phone_number.startswith("+"):
        return {"error": "Invalid phone number format. Use E.164 format (e.g., +1234567890)"}

    try:
        call = client.calls.create(
            to=phone_number,
            from_=TWILIO_PHONE,
            url="http://demo.twilio.com/docs/voice.xml"
        )
        return {"call_sid": call.sid}
    except Exception as e:
        return {"error": str(e)}
