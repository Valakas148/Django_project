import axios from "axios";
import {baseURL, urls} from "../constants/urls";


const apiService = axios.create({baseURL})

apiService.interceptors.request.use(req=>{
    const token = localStorage.getItem('access')

    // if (token && req.url !== `/${urls.users}` && req.url !== `${urls.auth.login}` && req.url !== `${urls.announcements}`) {
    //     req.headers.Authorization = `Bearer ${token}`;
    // }

    if (token && req.url !== `/${urls.users}` && req.url !== `${urls.auth.login}`) {
        req.headers.Authorization = `Bearer ${token}`;
    }

    return req
})

export {
    apiService
}