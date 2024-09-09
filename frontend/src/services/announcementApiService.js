import axios from "axios";
import {baseURL} from "../constants/urls";


const announcementApiService = axios.create({baseURL});

announcementApiService.interceptors.request.use(req => {
    const token = localStorage.getItem('access');

    if (token && req.method !== 'get') {
        req.headers.Authorization = `Bearer ${token}`;
    }

    return req;
}, error => {
    return Promise.reject(error);
});

export {
    announcementApiService
};
