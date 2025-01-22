import React, { useState, useEffect } from 'react';
import axios from 'axios'

export const UpdateQuantity = () => {
  const [htmlContent, setHtmlContent] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/update_quantity') // Specify Flask port
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
        "http://localhost:5000/update_quantity", // Replace with your actual update endpoint
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
        console.log("Quantity updated successfully");
        window.location.reload();
      } else {
        console.error("Error updating quantity:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <div dangerouslySetInnerHTML={{ __html: htmlContent }} />

      <div className="form">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            const formData = {
              ItemId: e.target.elements.ItemID.value,  // Access ItemID value
              Quantity: e.target.elements.Quantity.value,  // Access Quantity value
              option: e.target.elements.option.value,  // Access option value
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
          <label htmlFor="quantity_input">Quantity:</label>
          <input
            type="number"
            id="quantity_input"
            name="Quantity"
            min="1"
            max="10"
            required
          />
          <label htmlFor="add" className="addremove">
            Add
          </label>
          <input type="radio" id="add" name="option" value="Add" required />
          <label htmlFor="remove" className="addremove">
            Remove
          </label>
          <input type="radio" id="remove" name="option" value="Remove" required />
          <br />
          <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
  );
};
