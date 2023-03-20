import React, { useState, useContext, useEffect } from "react";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom"
import { ConnectionContext } from "../contexts/ConnectionContext";
import Api from "../utils/Api";
import { GoogleLogin } from "@react-oauth/google"

function SignIn() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [showPP, setShowPP] = useState("hide")

    const context = useContext(ConnectionContext)
    const navigate = useNavigate()
    const {t, i18n} = useTranslation()

    useEffect(() => {
        if(context.error === 401) {
            setShowPP("show")
            context.setError(200)
        }
    }, [])
    const hidePopup = e => {
        setShowPP("hide")
    }

    const submit = e => {
        e.preventDefault();

        Api.post('/authenticate', {
            email: email,
            password: password
        }, data => {
            Api.connect(context, data.token)
            navigate("/")
        }, context, false)
    }

    const google_con = response => {
        Api.post('/authenticate-ext', {
            ext_con_type: "GOOGLE",
            ext_con_id: response.credential
        }, data => {
            Api.connect(context, data.token)
            navigate("/")
        }, context, false)
    }

    return (
        <div id="sign-in">
            <div id="disconnected" className={showPP}>
                <div className="popup-content">
                    {t("signin.error.disconnected")}
                    <button onClick={hidePopup}>X</button>
                </div>
            </div>
            <form onSubmit={submit}>
                <h1>{t("signin.form.title")}</h1>
                <div className="group">
                    <input required={true} type="text" className="input" value={email} onChange={e => setEmail(e.target.value)} />
                    <span className="highlight"></span>
                    <span className="bar"></span>
                    <label>{t("signin.form.email")}</label>
                </div>
                <div className="group">
                    <input required={true} type="text" className="input" value={password} onChange={e => setPassword(e.target.value)} />
                    <span className="highlight"></span>
                    <span className="bar"></span>
                    <label>{t("signin.form.password")}</label>
                </div>
                <button type="submit">{t("signin.form.connect")}</button>
                <GoogleLogin onSuccess={google_con} />
            </form>
        </div>
    );
}

export default SignIn