const API_URL = process.env.REACT_APP_API_URL;

export const initiateCall = async (number) => {
    try {
        const response = await fetch(`${API_URL}/call/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ number }),
        });
        return await response.json();
    } catch (error) {
        console.error("Error initiating call:", error);
        return { error: "Failed to initiate call." };
    }
};

export const transcribeAudio = async () => {
    try {
        const response = await fetch(`${API_URL}/transcribe/`, { method: "POST" });
        return await response.json();
    } catch (error) {
        console.error("Error in transcription:", error);
        return { error: "Failed to transcribe audio." };
    }
};

export const analyzeObjections = async () => {
    try {
        const response = await fetch(`${API_URL}/analyze/`, { method: "POST" });
        return await response.json();
    } catch (error) {
        console.error("Error analyzing objections:", error);
        return { error: "Failed to analyze objections." };
    }
};

export const getLiveKitToken = async () => {
    try {
        const response = await fetch(`${API_URL}/get_livekit_token`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching LiveKit token:", error);
        return { error: "Failed to retrieve LiveKit token." };
    }
};
