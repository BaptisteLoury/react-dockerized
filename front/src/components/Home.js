import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { ConnectionContext } from "../contexts/ConnectionContext";
import Api from "../utils/Api";

function Home() {
    const con = useContext(ConnectionContext)
    const [infos, setInfos] = useState(null)
    const [expanded, setExpanded] = useState(false)

    useEffect(() => {
        if (con.connected) {
            Api.get('/user', data => {
                setInfos(data)
            }, con)
        }
    }, [con.connected])

    var sdbClas = expanded ? "expanded" : ""


    return (
        <div id="home">
            <div id="sidebar" className={sdbClas}>
                <div className="top">
                    <div className="hmbrg">
                        <input type="checkbox" id="menu_checkbox"
                            onChange={e => setExpanded(e.currentTarget.checked)} />
                        <label htmlFor="menu_checkbox">
                            <div></div>
                            <div></div>
                            <div></div>
                        </label>
                    </div>
                </div>
            </div>
            <div id="core">
                abc
            </div>
        </div>
    );
}

export default Home