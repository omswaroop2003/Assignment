import React, { useEffect, useState } from "react";
import { transcribeAudio } from "../api";

const Transcription = () => {
    const [transcription, setTranscription] = useState("");

    useEffect(() => {
        const fetchTranscription = async () => {
            const response = await transcribeAudio();
            setTranscription(response.transcription || "Waiting for transcription...");
        };

        const interval = setInterval(fetchTranscription, 3000); // Fetch every 3 seconds
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="transcription-container">
            <h2>Real-time Transcription</h2>
            <p>{transcription}</p>
        </div>
    );
};

export default Transcription;
