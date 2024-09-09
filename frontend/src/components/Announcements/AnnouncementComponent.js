import React from 'react';

const AnnouncementComponent = ({announcement}) => {


    return (
        <div>
            <p>Announcment №{announcement.id} -- CAR: {announcement.car}</p>
            <p>{announcement.original_price} {announcement.original_currency}</p>
            <p>{announcement.place}</p>
            <p>{announcement.description}</p>
            <hr/>
        </div>
    );
};

export default AnnouncementComponent;