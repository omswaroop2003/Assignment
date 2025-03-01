import React from "react";
import CallLiveKitIntegration from "./components/CallLiveKitIntegration";
import Transcription from "./components/Transcription";
import ObjectionAnalysis from "./components/ObjectionAnalysis";

function App() {
    return (
        <div className="app-container">
            <h1>Real-Time Call Handling</h1>
            <CallLiveKitIntegration />
            <Transcription />
            <ObjectionAnalysis />
        </div>
    );
}

export default App;
