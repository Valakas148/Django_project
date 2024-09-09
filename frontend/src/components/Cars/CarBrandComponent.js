import React from 'react';

const CarBrandComponent = ({brand}) => {
    return (
        <div>
            <p>Brand №{brand.id}</p>
            <p>brand - {brand.name}</p>
        </div>
    );
};

export default CarBrandComponent;