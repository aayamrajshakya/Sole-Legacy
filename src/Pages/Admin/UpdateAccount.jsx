import React, { useState, useEffect } from 'react';
import axios from 'axios'

export const UpdateAccount = () => {
  const [htmlContent, setHtmlContent] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/update_form'); // Specify Flask port
        const data = await response.text();
        setHtmlContent(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async (formData) => {
    try {
      const response = await axios.post(
        "http://localhost:5000/update_form", // Replace with your actual update endpoint
        formData,
        {
          withCredentials: true,
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      if (response.status === 200) {
        // Handle successful update (e.g., re-fetch data, show message)
        console.log("Account Updated Successfully");
        window.location.reload();
      } else {
        console.error("Error Updating Account:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="User_container">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            const formData = {
              FullName: e.target.elements.FullName.value,
              Email: e.target.elements.Email.value,
              Address: e.target.elements.Address.value,
              Password: e.target.elements.Password.value,
            };
            handleSubmit(formData);
          }}
        >
          <label htmlFor="name-input">Full Name:</label>
          <input type="text" id="name-input" name="FullName" />
          <br />
          <label htmlFor="email-input">Email Address:</label>
          <input type="text" id="email-input" name="Email" />
          <br />
          <label htmlFor="address-input">Address:</label>
          <input type="text" id="address-input" name="Address" />
          <br />
          <label htmlFor="password-input">Password:</label>
          <input type="text" id="password-input" name="Password" />
          <br />
          <input type="submit" value="Submit" />
        </form>
      </div>
  );
};
