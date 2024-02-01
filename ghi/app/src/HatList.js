import React, { useState, useEffect } from 'react';

function HatList() {
    const [hats, setHats] = useState([]);

    const getData = async () => {
        const response = await fetch("http://localhost:8090/api/hats");

        if (response.ok) {
            const data = await response.json();
            setHats(data.hats);
        }
    }

    useEffect(()=>{
        getData()
    }, [])

    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Fabric</th>
                    <th>Style Name</th>
                    <th>Color</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                {hats.map(hat => {
                    return (
                        <tr key={hat.id}>
                            <td>{hat.fabric}</td>
                            <td>{hat.style_name}</td>
                            <td>{hat.color}</td>
                            <td>{hat.location ? hat.location.import_href : 'No location'}</td>
                        </tr>
                    )
                } )}
            </tbody>
        </table>
    )
}

export default HatList;
