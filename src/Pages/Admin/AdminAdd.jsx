import React, { useState } from "react";
import axios from "axios";


export const AdminAdd = () => {
  const [formData, setFormData] = useState({
    ItemName: "",
    Quantity: 1,
    Price: "",
    Gender: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log(formData)
        const response = await
   axios.post(
          "http://localhost:5000/admin_add",

          formData,
          {
            withCredentials: true,
            headers:{
              'Content-Type': 'multipart/form-data'
            }
          }
        );

        if (response.status === 200) {
          console.log("Success:", response.data);
          window.location.reload();
          setFormData({
            ItemName: "",
            Quantity: 1,
            Price: "",
            Gender: "",
          });
        } else {
          console.error("Error:", response.status);
        }
      } catch (error) {
        console.error("Error:", error);
      }
    };

    return (
      <div className="User_container">
        <form onSubmit={handleSubmit}>
          <caption>Add item form</caption>
          <div>
            <label htmlFor="item-name">Item Name:</label>
            <input
              type="text"
              id="item-name"
              name="ItemName"
              value={formData.ItemName}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="number"
              id="quantity"
              name="Quantity"

              value={formData.Quantity}
              onChange={handleChange}
              min="1"

              max="10"
              required
            />
          </div>
          <div>
            <label htmlFor="price">Price:</label>
            <input
              type="text"
              id="price"
              name="Price"
              value={formData.Price}
              onChange={handleChange}

              required
            />
          </div>
          <div>
            <label htmlFor="gender">Gender:</label>
            <input
              type="text"
              id="gender"
              name="Gender"
              value={formData.Gender}
              onChange={handleChange}
              required
            />
          </div>

          <button type="submit">Submit</button>
        </form>
      </div>

    );
  };