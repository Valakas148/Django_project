import React, {useState} from 'react';
import {useNavigate} from "react-router-dom";
import {carService} from "../../services/carService";

const CarCreateFormComponent = () => {
    const [form, setForm] = useState({
        brand : '',
        model : '',
        year : '',
        body_type : ''
    });

    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);
    const navigate = useNavigate()

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setForm({
            ...form,
            [name]: value
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await carService.createCars(form);
            setSuccess('Announcement created successfully!');
            setError(null);
            navigate('')
        } catch (error) {
            console.error("Error creating announcement:", error);
            setError('Failed to create announcement. Please try again.');
            setSuccess(null);
        }
    };
    return (
        <div>
            <h2>Create Car</h2>

            {error && <p style={{color: 'red'}}>{error}</p>}
            {success && <p style={{color: 'green'}}>{success}</p>}

            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="brand">Name Brand:</label>
                    <input
                        type="text"
                        id="brand"
                        name="brand"
                        value={form.brand}
                        onChange={handleInputChange}
                        required
                    />
                </div>


                <div>
                    <label htmlFor="model">Name Model:</label>
                    <input
                        type="text"
                        id="model"
                        name="model"
                        value={form.model}
                        onChange={handleInputChange}
                        required
                    />
                </div>


                <div>
                    <label htmlFor="year">Year:</label>
                    <input
                        type="number"
                        id="year"
                        name="year"
                        value={form.year}
                        onChange={handleInputChange}
                        required
                    />
                </div>

                <div>
                    <label htmlFor="body_type">Body Type:</label>
                    <input
                        type="text"
                        id="body_type"
                        name="body_type"
                        value={form.body_type}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <button type="submit">Create Brand</button>
            </form>
        </div>
    );
};

export default CarCreateFormComponent;