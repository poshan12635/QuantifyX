import React from "react";
import './Navbar.css'


function Navbar(){
    return(
        <>
        <nav className="nabar">
            <ul className="list">
                <li className="home"><a href="#">Home</a></li>
                <li className="Backtest"><a href="#">Backtest</a></li>
                <li className="ai"><a href="#">Ai recomendation</a></li>
                <li className="portfolio"><a href="#">Portfolio Management</a></li>

            </ul>

        </nav>
        
        
        </>
    );
}
export default Navbar