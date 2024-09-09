import React from 'react';

const CarComponent = ({car}) => {
    return (
        <div>
            <p>Cars №{car.id}</p>
            <p>brand - {car.brand}</p>
            <p>model - {car.model}</p>
            <p>year - {car.year}</p>
            <p>body_type - {car.body_type}</p>
            <hr/>
        </div>
    );
};

export default CarComponent;