import React, { useEffect, useState, Suspense } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
import './style/App.scss'
import Home from "./components/Home";
import SignIn from "./components/SignIn";
import SignUp from "./components/SignUp";
import { ConnectionContext } from "./contexts/ConnectionContext";

function App() {
    const [connected, setConnected] = useState(false)
    const [error, setError] = useState(200)

    const navigate = useNavigate()

    useEffect(() => {
        if (!connected) {
            if (sessionStorage.getItem('jwt') !== null) {
                setConnected(true)
            } else {
                navigate("/sign-in")
            }
        }
    }, [connected])

    return (
        <Suspense fallback="loading">
            <ConnectionContext.Provider value={{
                connected: connected,
                setConnected: setConnected,
                error: error,
                setError: setError
            }}>
                <Routes>
                    <Route path="/">
                        <Route index element={<Home />} />
                        <Route path="sign-in" element={<SignIn />} />
                        <Route path="sign-up" element={<SignUp />} />
                    </Route>
                </Routes>
            </ConnectionContext.Provider>
        </Suspense>
    );
}

export default App