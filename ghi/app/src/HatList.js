import React, { useState, useEffect } from 'react';

function HatList() {
    const [hats, setHats] = useState([]);
    const [locations, setLocations] = useState({});

    const fetchHats = async () => {
        try {
            const response = await fetch("http://localhost:8090/api/hats");
            const data = await response.json();
            setHats(data.hats);
        } catch (error) {
            console.error('Error fetching locations:', error);
        }
    };

    const fetchLocations = async () => {
        try {
            const response = await fetch("http://localhost:8100/api/locations");
            const data = await response.json();
            const locationsMap = data.locations.reduce((acc, location) => {
                acc[location.href] = `${location.closet_name} - ${location.section_number}/${location.shelf_number}`;
                return acc;
            }, {});
            setLocations(locationsMap);
        } catch (error) {
            console.error('Error fetching locations:', error);
        }
    };

    useEffect(()=>{
        fetchHats();
        fetchLocations();
    }, []);

    return (
        <div className="shadow p-4 mt-4">
            <h1>Hat List</h1>
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
                        const locationString = hat.location ? locations[hat.location.import_href] : 'No location';
                        return (
                            <tr key={hat.id}>
                                <td>{hat.fabric}</td>
                                <td>{hat.style_name}</td>
                                <td>{hat.color}</td>
                                <td>{locationString || 'Loading location...'}</td>
                            </tr>
                        )
                    } )}
                </tbody>
            </table>
        </div>
    )
}

export default HatList;
