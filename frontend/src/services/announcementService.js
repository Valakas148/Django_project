import {urls} from "../constants/urls";
import {announcementApiService} from "./announcementApiService";


const announcementService = {
    getAll(){
        return announcementApiService.get(urls.announcements)
    },
    create(announcement){
        return announcementApiService.post(urls.announcements, announcement)
    }
}

export {
    announcementService
}