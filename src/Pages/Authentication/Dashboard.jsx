// Much help from: https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/

import React, { useState, useEffect } from "react";
import './Dashboard.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import logout_icon from "../../Components/Assets/general/logout.png"
import delete_icon from "../../Components/Assets/general/delete.png"

export const Dashboard = () => {
    const navigate = useNavigate();

    const handleLogout = async () => {
      try {
        const response = await axios.post('http://localhost:5000/logout', {}, {
          withCredentials: true,
        });
        alert(response.data.message);
        navigate("/");   // take user to homepage after logging out
      } catch (error) {
        alert(error.response?.data?.error || "Flask server offline");
      }
    };

    const handleDelete = async () => {
        try {
          const response = await axios.post('http://localhost:5000/delete', {}, {
            withCredentials: true,
          });
          alert(response.data.message);
          navigate("/");   // take user to homepage after logging out
        } catch (error) {
          alert(error.response?.data?.error || "Flask server offline");
        }
      };
  

    const [data, setData] = useState({
        AccountID: null,
        Name: "",
        EmailAddress: "",
        HomeAddress: "",
        UserRole: "",
    });

    useEffect(() => {
        const userDetails = async () => {
            try {
                const response = await axios.get('http://localhost:5000/dashboard', {
                    withCredentials: true
                });
                setData(response.data);
            } catch (error) {
                alert(error.response?.data?.error || "Flask server offline");
            }
        };

        userDetails();
    }, []);

    return (
    <div className="dashboard_page">
        <h3>User Dashboard</h3>
        <table id="infoTable">
            <tr>
              <th>Parameter</th>
              <th>Value</th>
            </tr>
            <tr>
              <td>Account ID</td>
              <td>{data.AccountID || "N/A"}</td>
            </tr>
            <tr>
              <td>Name</td>
              <td>{data.Name || "N/A"}</td>
            </tr>
            <tr>
              <td>Email Address</td>
              <td>{data.EmailAddress || "N/A"}</td>
            </tr>
            <tr>
              <td>Home Address</td>
              <td>{data.HomeAddress || "N/A"}</td>
            </tr>
            <tr>
              <td>User Type</td>
              <td>{data.UserRole || "N/A"}</td>
            </tr>
        </table>
        <button class="action_btn" role="button" onClick={handleLogout}>Log out <img src={logout_icon} /></button>
        <button class="action_btn" role="button" onClick={handleDelete}>Delete <img src={delete_icon} /></button>

    </div>
    );
}