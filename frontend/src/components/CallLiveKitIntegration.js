import React, { useState, useEffect } from "react";
import { initiateCall, transcribeAudio } from "../api";
import { LiveKitRoom, VideoConference } from "@livekit/components-react";
import "@livekit/components-styles";


const CallLiveKitIntegration = () => {
    const [number, setNumber] = useState("");
    const [callStatus, setCallStatus] = useState("");
    const [token, setToken] = useState("");

    useEffect(() => {
        const getToken = async () => {
            try {
                const response = await fetch("http://localhost:8000/get_livekit_token");
                const data = await response.json();
                setToken(data.token);
            } catch (error) {
                console.error("Error fetching LiveKit token:", error);
            }
        };

        getToken();
    }, []);

    const handleCall = async () => {
        if (!number) {
            setCallStatus("Please enter a valid phone number");
            return;
        }

        try {
            const response = await initiateCall(number);
            setCallStatus(`Call initiated with SID: ${response.call_sid}`);
        } catch (error) {
            setCallStatus("Error initiating call");
        }
    };

    return (
        <div className="call-livekit-container">
            <h2>Call & Real-time Streaming</h2>
            <input
                type="text"
                placeholder="Enter phone number"
                value={number}
                onChange={(e) => setNumber(e.target.value)}
            />
            <button onClick={handleCall}>Start Call</button>
            <p>{callStatus}</p>

            {token ? (
                <LiveKitRoom serverUrl={process.env.REACT_APP_LIVEKIT_URL} token={token}>
                    <VideoConference />
                </LiveKitRoom>
            ) : (
                <p>Loading LiveKit...</p>
            )}
        </div>
    );
};

export default CallLiveKitIntegration;
