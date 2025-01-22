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
            const response = await axios.post('http://localhost:5000/search', { searchKeyword }, {
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
        <div className="view_search_container">
            <div className="search_page">
                <h3>Search</h3>
                <form onSubmit={handleSearch} className="search_form">
                    <div className="search_input">
                        <input className="search_box" type="text" value={searchKeyword} onChange={(e) => setSearchKeyword(e.target.value)} placeholder="Search an item" required />
                        <button type="submit" className='search_btn'><img src={search_icon} /></button>
                    </div>
                </form>
            </div>

            {resultItems.length > 0 && (
                <div className="search_grid">
                    {resultItems.map((item) => (
                        <div key={item.ItemID} className="search_card">
                            <div className="search_image">
                                <img src={`${process.env.PUBLIC_URL}/${item.Gender}/${item.Image}`} alt={item.ItemName} />
                            </div>
                            <div className="search_details">
                                <h3>{item.ItemName}</h3>
                                <div className="search_meta">
                                    <span className="item_price">${item.Price}</span>
                                    <span className="item_gender">{item.Gender}</span>
                                </div>
                                <Link to={`/${item.Gender}/${item.Url}`}><p className='item_link'>View product</p></Link>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    )
};