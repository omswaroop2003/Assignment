import React, { useEffect, useState } from "react";
import { LiveKitRoom, VideoConference } from "@livekit/components-react";
import { getLiveKitToken } from "../api";
import "@livekit/components-styles";

const LIVEKIT_URL = process.env.REACT_APP_LIVEKIT_URL

const LiveKitComponent = () => {
    const [token, setToken] = useState("");

    useEffect(() => {
        const fetchToken = async () => {
            const data = await getLiveKitToken();
            if (!data.error) setToken(data.token);
        };
        fetchToken();
    }, []);

    return (
        <div className="container">
            <h2>Live Call Streaming</h2>
            {token ? (
                <LiveKitRoom serverUrl={LIVEKIT_URL} token={token}>
                    <VideoConference />
                </LiveKitRoom>
            ) : (
                <p>Loading LiveKit...</p>
            )}
        </div>
    );
};

export default LiveKitComponent;
