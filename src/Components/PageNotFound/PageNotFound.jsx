// Reference from: https://www.geeksforgeeks.org/how-to-setup-404-page-in-react-routing/

import React from "react";
import './PageNotFound.css';

export const PageNotFound = () => {
    return (
        <div className="error_page">
            <h1>Error</h1>
            <p className="error_code"><b>404</b></p>
            <h3>Oops! The page you requested could not be found.</h3>
        </div>
    )
}
