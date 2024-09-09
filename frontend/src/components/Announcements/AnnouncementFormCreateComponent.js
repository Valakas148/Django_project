import React, {useEffect, useState} from 'react';
import { announcementService } from "../../services/announcementService";
import {useNavigate} from "react-router-dom";
import {carService} from "../../services/carService";

const AnnouncementFormCreateComponent = () => {
    const [form, setForm] = useState({
        // car: '',
        brand: '',
        model: '',
        year: '',
        body_type: '',
        original_currency: 'USD',
        original_price: '',
        place: '',
        description: ''
    });

    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);
    const [carOptions, setCarOptions] = useState([]);
    const navigate = useNavigate()


    useEffect(() => {
        carService.getAllCars().then(({ data }) => {
            if (Array.isArray(data.data)) {
                console.log("Cars found:", data.data);
                setCarOptions(data.data);
            } else {
                setCarOptions([]);
            }
        }).catch(error => {
            console.error("Error fetching cars:", error);
            setCarOptions([]);
        });
    }, []);


    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setForm({
            ...form,
            [name]: value
        });
    };
    const handleSubmit = async (event) => {
        event.preventDefault();

        const selectedCar = carOptions.find(car =>
            car.brand === form.brand &&
            car.model === form.model &&
            car.year.toString() === form.year.toString() &&
            car.body_type === form.body_type
        );

        if (!selectedCar) {
            setError("Car not found. Please check the details.");
            return;
        }

        try {
            const response = await announcementService.create({
                ...form,
                car: selectedCar.id
            });
            setSuccess('Announcement created successfully!');
            setError(null);
            navigate('/announcements');
        } catch (error) {
            console.error("Error creating announcement:", error);
            setError('Failed to create announcement. Please try again.');
            setSuccess(null);
        }
    };

    console.log("Form data:", form);

    return (
        <div>
            <h2>Create Announcement</h2>

            {error && <p style={{ color: 'red' }}>{error}</p>}
            {success && <p style={{ color: 'green' }}>{success}</p>}

            <form onSubmit={handleSubmit}>

                {/*<div>*/}
                {/*    <label htmlFor="car">Car ID:</label>*/}
                {/*    <input*/}
                {/*        type="number"*/}
                {/*        id="car"*/}
                {/*        name="car"*/}
                {/*        value={form.car}*/}
                {/*        onChange={handleInputChange}*/}
                {/*        required*/}
                {/*    />*/}
                {/*</div>*/}

                <div>
                    <label htmlFor="brand">Car Brand:</label>
                    <select
                        id="brand"
                        name="brand"
                        value={form.brand}
                        onChange={handleInputChange}
                        required
                    >
                        <option value="">Select Brand</option>
                        {carOptions.map((car) => (
                            <option key={car.id} value={car.brand}>
                                {car.brand}
                            </option>
                        ))}
                    </select>
                </div>

                <div>
                    <label htmlFor="model">Car Model:</label>
                    <select
                        id="model"
                        name="model"
                        value={form.model}
                        onChange={handleInputChange}
                        required
                    >
                        <option value="">Select Model</option>
                        {carOptions
                            .filter((car) => car.brand === form.brand)
                            .map((car) => (
                                <option key={car.id} value={car.model}>
                                    {car.model}
                                </option>
                            ))}
                    </select>
                </div>

                <div>
                    <label htmlFor="year">Year:</label>
                    <select
                        id="year"
                        name="year"
                        value={form.year}
                        onChange={handleInputChange}
                        required
                    >
                        <option value="">Select Year</option>
                        {carOptions
                            .filter((car) => car.brand === form.brand && car.model === form.model)
                            .map((car) => (
                                <option key={car.id} value={car.year}>
                                    {car.year}
                                </option>
                            ))}
                    </select>
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

                <div>
                    <label htmlFor="original_currency">Currency:</label>
                    <select
                        id="original_currency"
                        name="original_currency"
                        value={form.original_currency}
                        onChange={handleInputChange}
                        required
                    >
                        <option value="USD">USD</option>
                        <option value="EUR">EUR</option>
                        <option value="UAH">UAH</option>
                    </select>
                </div>

                <div>
                    <label htmlFor="original_price">Price:</label>
                    <input
                        type="number"
                        id="original_price"
                        name="original_price"
                        value={form.original_price}
                        onChange={handleInputChange}
                        required
                    />
                </div>

                <div>
                    <label htmlFor="place">Place:</label>
                    <input
                        type="text"
                        id="place"
                        name="place"
                        value={form.place}
                        onChange={handleInputChange}
                        required
                    />
                </div>

                <div>
                    <label htmlFor="description">Description:</label>
                    <textarea
                        id="description"
                        name="description"
                        value={form.description}
                        onChange={handleInputChange}
                        required
                    />
                </div>

                <button type="submit">Create Announcement</button>
            </form>
        </div>
    );
};

export default AnnouncementFormCreateComponent;
