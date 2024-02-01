import React, {useState, useEffect} from 'react';

function HatForm() {

    const[locations, setLocations] = useState([])
    const[formData, setFormData] = useState({
        fabric: '',
        style_name: '',
        color: '',
        picture_url: '',
        location: ''
    })

    const getData = async () => {
        const url = "http://localhost:8100/api/locations/";
        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            setLocations(data.locations);
        }

    }

    useEffect(()=> {
        getData();
    }, [])

    const handleSubmit = async (event) => {
        event.preventDefault();

        const hatUrl = "http://localhost:8090/api/hats/";

        const fetchConfig = {
            method: "post",
            body: JSON.stringify(formData),
            headers: {
                'Content-Type': 'application/json',
            },
        };

        const response = await fetch(hatUrl, fetchConfig);

        if (!response.ok) {
            const errorData = await response.text();
            console.log("Server response error:", errorData);
        }

        if (response.ok) {
            setFormData({
                fabric: '',
                style_name: '',
                color: '',
                picture_url: '',
                location: ''
            });
        }
    }

    const handleFormChange = (e) => {
        const value = e.target.value;
        const inputName = e.target.name;
        setFormData({
            //Previous form data is spread (i.e. copied) into our new state object
            ...formData,

            //On top of the that data, we add the currently engaged input key and value
            [inputName]: value
        });
    }

    return (
        <div className="row">
          <div className="offset-3 col-6">
            <div className="shadow p-4 mt-4">
              <h1>Create a new hat</h1>
              <form onSubmit={handleSubmit} id="create-hat-form">
                <div className="form-floating mb-3">
                  <input value={formData.fabric} onChange={handleFormChange} placeholder="Fabric" required type="text" name="fabric" id="fabric" className="form-control" />
                  <label htmlFor="fabric">Fabric</label>
                </div>
                <div className="form-floating mb-3">
                  <input value={formData.style_name} onChange={handleFormChange} placeholder="Style Name" required type="text" name="style_name" id="style_name" className="form-control" />
                  <label htmlFor="style_name">Style Name</label>
                </div>
                <div className="form-floating mb-3">
                  <input value={formData.color} onChange={handleFormChange} placeholder="Color" required type="text" name="color" id="color" className="form-control" />
                  <label htmlFor="color">Color</label>
                </div>
                <div className="form-floating mb-3">
                  <input value={formData.picture_url} onChange={handleFormChange} placeholder="Picture URL" required type="text" name="picture_url" id="picture_url" className="form-control" />
                  <label htmlFor="picture_url">Picture URL</label>
                </div>
                <div className="mb-3">
                  <select value={formData.location} onChange={handleFormChange} required name="location" id="location" className="form-select">
                    <option value="">Choose a location</option>
                    {locations.map(location => {
                      return (
                        <option key={location.id} value={location.id}>
                          {location.closet_name} - {location.section_number}/{location.shelf_number}
                        </option>
                      );
                    })}
                  </select>
                </div>
                <button className="btn btn-primary">Create</button>
              </form>
            </div>
          </div>
        </div>
      );
}

export default HatForm;
