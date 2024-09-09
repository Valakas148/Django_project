import React from 'react';
import CarsComponents from "../components/Cars/CarsComponents";
import CarBrandsComponent from "../components/Cars/CarBrandsComponent";
import CarBrandFormCreateComponent from "../components/Cars/CarBrandFormCreateComponent";
import CarCreateFormComponent from "../components/Cars/CarCreateFormComponent";

const CarAdminPage = () => {
    return (
        <div>
            <p>Only for admins:</p>
            <CarBrandFormCreateComponent/>
            <CarBrandsComponent/>
            <hr/>
            <br/>
            <CarCreateFormComponent/>
            <CarsComponents/>
        </div>
    );
};

export default CarAdminPage;