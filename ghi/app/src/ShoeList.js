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

  async function handleDelete(id) {
    const fetchOptions = { method: "DELETE" };
    const request = await fetch(`http://localhost:8080/api/shoes/${id}/`, fetchOptions);
    if (request.ok) {
      const data = await request.json();
      alert(`Shoe with ID ${id} has been deleted`);
      fetchShoeData();
    } else {
      alert(`Failed to delete shoe with ID ${id}`);
    }
  }

  return (
    <div>
      <h1>Shoe List</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Model Name</th>
            <th>Manufacturer</th>
            <th>Color</th>
            <th>Bin</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {shoes.map((shoe) =>
            <tr key={shoe.id}>
              <td>{shoe.model_name}</td>
              <td>{shoe.manufacturer}</td>
              <td>{shoe.color}</td>
              <td>{shoe.bin}</td>
              <td>
                <button onClick={() => handleDelete(shoe.id)} className="btn btn-danger">Delete</button>
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default ShoeList;
