import os
import torchaudio
from transformers import pipeline

# Load Whisper model
whisper_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def convert_to_wav(audio_path):
    """Converts MP3 to WAV if necessary"""
    if audio_path.lower().endswith(".wav"):
        return audio_path  # No conversion needed

    wav_path = audio_path.rsplit(".", 1)[0] + ".wav"  # Change extension
    torchaudio.set_audio_backend("soundfile")

    try:
        waveform, sample_rate = torchaudio.load(audio_path)
        torchaudio.save(wav_path, waveform, sample_rate)  # Save as WAV
        return wav_path
    except Exception as e:
        print(f"Error converting audio: {e}")
        return None  # Return None on failure

def transcribe_audio(audio_path):
    """Transcribes an audio file using Whisper."""
    if not os.path.exists(audio_path):
        return {"error": "Audio file not found"}

    try:
        wav_path = convert_to_wav(audio_path)
        if not wav_path:
            return {"error": "Failed to convert audio to WAV"}

        result = whisper_model(wav_path)  # Transcribe
        return {"transcription": result["text"]}
    except Exception as e:
        return {"error": f"Transcription failed: {str(e)}"}
