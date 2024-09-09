import {apiService} from "./apiService";
import {urls} from "../constants/urls";


const carService = {
    getAllBrands(){
        return apiService.get(urls.cars.brands)
    },
    getAllCars(){
        return apiService.get(urls.cars.models)
    },
    create(data){
        console.log(data)
        return apiService.post(urls.cars.brands, data)
    },
    createCars(data){
        console.log(data)
        return apiService.post(urls.cars.models, data)
    }
}

export {
    carService
}