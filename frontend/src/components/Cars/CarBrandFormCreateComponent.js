import React, {useState} from 'react';
import {useNavigate} from "react-router-dom";
import {announcementService} from "../../services/announcementService";
import {carService} from "../../services/carService";

const CarBrandFormCreateComponent = () => {
    const [form, setForm] = useState({
        name: '',
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
            const response = await carService.create(form);
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
            <h2>Create Brand</h2>

            {error && <p style={{color: 'red'}}>{error}</p>}
            {success && <p style={{color: 'green'}}>{success}</p>}

            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Name Brand:</label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                        value={form.name}
                        onChange={handleInputChange}
                        required
                    />
                </div>
                <button type="submit">Create Brand</button>
            </form>
        </div>
    );
};

export default CarBrandFormCreateComponent;