import React, { useState, useEffect } from "react";
import axios from "axios";


export const RemoveItem = () => {
  const [htmlContent, setHtmlContent] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:5000/admin_remove");
        const data = await response.text();
        setHtmlContent(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  // Function to handle the update form submission
  const handleSubmit = async (formData) => {
    try {
      const response = await axios.post(
        "http://localhost:5000/admin_remove", // Replace with your actual update endpoint
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
        console.log("Item Removed Successfully");
        window.location.reload();
      } else {
        console.error("Error Removing Item:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <div dangerouslySetInnerHTML={{ __html: htmlContent }} />

      {/* Additional form from your HTML, modified for React */}
      <div className="form">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            // Gather form data and call handleUpdateSubmit
            const formData = {
              ItemId: e.target.ItemID.value
            };
            handleSubmit(formData);
          }}
        >
          <caption className="form_caption">
            Please enter the item you would like to remove:
          </caption>
          <br /><br />
          <label htmlFor="ItemId_input">Item ID:</label>
          <input type="text" id="ItemId_input" name="ItemID" required />
          <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
  );
};