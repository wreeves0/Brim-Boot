import React, { useState, useEffect } from 'react';

function ShoeList() {
  const [shoes, setShoes] = useState([]);


  const fetchShoeData = async () => {
    const url = 'http://localhost:8080/api/shoes/';
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setShoes(data.shoes);
    }
  };

  useEffect(() => {
    fetchShoeData();
  }, []);

  return (
    <div>
      <h1>Shoe List</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Manufacturer</th>
            <th>Model Name</th>
          </tr>
        </thead>
        <tbody>
          {shoes.map((shoe) => (
            <tr key={shoe.id}>
              <td>{shoe.manufacturer}</td>
              <td>{shoe.model_name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ShoeList;
