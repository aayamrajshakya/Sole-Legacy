// almost similar to wishlist page

import React, { useState } from 'react';
import './Search.css';
import search_icon from "../../Components/Assets/general/search.png";
import axios from 'axios';
import { Link } from "react-router-dom";

export const Search = () => {
    const [searchKeyword, setSearchKeyword] = useState('');
    const [resultItems, setResultItems] = useState([]);     // result items set to empty initially

    const handleSearch = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://localhost:5000/search', {searchKeyword}, {
                headers: {
                    'Content-Type': 'application/json',
                },
                withCredentials: true,
            });
            setResultItems(response.data.items || []);
        } catch (error) {
            alert(error.response?.data?.error || "Flask server offline");
            setResultItems([]);
        }
    };

  return (
    <div className='search_page'>
        <h3>Search</h3>
        <form onSubmit={handleSearch}>
        <label htmlFor="search_item"></label>
        <input className="search_box" placeholder='Search an item' type="text" value={searchKeyword} onChange={(e) => setSearchKeyword(e.target.value)} required/>
        <button type="submit" className='search_btn'><img src = {search_icon} /></button>
    </form>
            {resultItems.length === 0 ? (<p>No matching item found</p>) : (
                <div className="search_main_container">
                    {resultItems.map((item) => (
                        <div key={item.ItemID} className="search_view">
                            <img className="item_image" src={`${process.env.PUBLIC_URL}/${item.Gender}/${item.Image}`} />
                            <p className="item_name"><b>{item.ItemName}</b></p>
                            <div className="item_details">
                            <p className="item_gender"><b>Gender:</b> {item.Gender}</p>  
                            <p className="item_price"><b>Price:</b> ${item.Price}</p>
                        </div>
                        <Link to={`/${item.Gender}/${item.Url}`}><p className='viewText'>View product</p></Link>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};