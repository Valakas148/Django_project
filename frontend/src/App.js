import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [anns, setAnn] = useState([])


    useEffect(() => {
        axios.get('/api/announcements').then(({data}) => setAnn(data.data))
    }, [])

    return (
        <div>
            {anns.map(ann=><div key={ann.id}>
                <p>Announcment №{ann.id} -- CAR: {ann.car}</p>
                <p>{ann.original_price} {ann.original_currency}</p>
                <p>{ann.place}</p>
                <p>{ann.description}</p>
                <hr/>
            </div>)}
        </div>
    );
};

export {App};