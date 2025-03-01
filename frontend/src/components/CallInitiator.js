import React, { useState } from "react";
import { initiateCall } from "../api";

const CallInitiator = () => {
    const [number, setNumber] = useState("");
    const [callStatus, setCallStatus] = useState("");

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
        <div className="call-container">
            <h2>Initiate Call</h2>
            <input
                type="text"
                placeholder="Enter phone number"
                value={number}
                onChange={(e) => setNumber(e.target.value)}
            />
            <button onClick={handleCall}>Call</button>
            <p>{callStatus}</p>
        </div>
    );
};

export default CallInitiator;
        