import React, {useEffect, useState} from 'react';
import {carService} from "../../services/carService";
import CarComponent from "./CarComponent";
import CarBrandComponent from "./CarBrandComponent";

const CarBrandsComponent = () => {
    const [brands, setBrands] = useState([])

    useEffect(() => {
        carService.getAllBrands().then(({ data }) => {
            if (Array.isArray(data.data)) {
                setBrands(data.data);
            } else {
                console.error("Expected an array but got:", data.data);
                setBrands([]);
            }
        }).catch(error => {
            console.error("Error fetching announcements:", error);
            setBrands([]);
        });
    }, []);

    return (
        <div>
            <h3>Existing Brands</h3>
            {
                brands.map(brand=><CarBrandComponent key={brand.id} brand={brand}/> )
            }
        </div>
    );
};

export default CarBrandsComponent;