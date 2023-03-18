import React, { useState } from "react";

function SignUp() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const submit = e => {
        e.preventDefault();
    }

    return (
        <div id="sign-up">
            <form onSubmit={submit}>
                <label>
                    Email:
                    <input type="text" value={email} onChange={e => setEmail(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                </label>
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default SignUp