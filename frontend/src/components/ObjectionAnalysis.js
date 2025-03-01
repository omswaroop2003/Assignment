import React, { useState } from "react";

const ObjectionAnalysis = ({ transcription }) => {
    const [objections, setObjections] = useState("");
    const [selectedResponse, setSelectedResponse] = useState("");
    const [agentNotes, setAgentNotes] = useState("");

    const submitFeedback = async () => {
        try {
            const response = await fetch("http://localhost:8000/submit_feedback/", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({
                    objection: objections,
                    selected_response: selectedResponse,
                    agent_notes: agentNotes,
                }),
            });

            const data = await response.json();
            alert(data.message || "Feedback submitted.");
        } catch (error) {
            alert("Error submitting feedback.");
        }
    };

    return (
        <div className="objection-container">
            <h2>Objection Analysis</h2>
            <p>{transcription || "Waiting for transcription..."}</p>

            <h3>Provide Feedback</h3>
            <input type="text" placeholder="Selected Response" value={selectedResponse} onChange={(e) => setSelectedResponse(e.target.value)} />
            <textarea placeholder="Agent Notes" value={agentNotes} onChange={(e) => setAgentNotes(e.target.value)} />
            <button onClick={submitFeedback}>Submit Feedback</button>
        </div>
    );
};

export default ObjectionAnalysis;
