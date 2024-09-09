import React, {useEffect, useState} from 'react';
import {carService} from "../../services/carService";
import CarComponent from "./CarComponent";
import {announcementService} from "../../services/announcementService";

const CarsComponents = () => {
    const [cars, setCars] = useState([])

    useEffect(() => {
        carService.getAllCars().then(({ data }) => {
            if (Array.isArray(data.data)) {
                setCars(data.data);
            } else {
                console.error("Expected an array but got:", data.data);
                setCars([]);
            }
        }).catch(error => {
            console.error("Error fetching announcements:", error);
            setCars([]);
        });
    }, []);


    return (
        <div>
            <h3>Existing Cars</h3>
            {
                cars.map(car=><CarComponent key={car.id} car={car}/> )
            }
        </div>
    );
};

export default CarsComponents;