import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css'; // Import your CSS file

function Data() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://your-django-api-url/data/')
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Data List</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id} className="flex-container">
            <div>
              <span className="label">Temperature:</span> {item.temperature}
            </div>
            <div>
              <span className="label">Humidity:</span> {item.humidity}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Data;
