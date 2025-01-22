import React, { useState, useEffect } from 'react';
import '../../static/table.css'

export const UserDirectory = () => {
  const [htmlContent, setHtmlContent] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/admin_view'); // Specify Flask port
        const data = await response.text();
        setHtmlContent(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);


  return (
    <div>
      <div dangerouslySetInnerHTML={{ __html: htmlContent }} />
    </div>
  );
};
