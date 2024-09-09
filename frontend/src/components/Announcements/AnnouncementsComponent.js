import React, {useEffect, useState} from 'react';
import {announcementService} from "../../services/announcementService";
import AnnouncementComponent from "./AnnouncementComponent";
import {socketService} from "../../services/socketService";

const AnnouncementsComponent = () => {

    const[announcements, SetAnnouncements] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        announcementService.getAll().then(({ data }) => {
            if (Array.isArray(data.data)) {
                SetAnnouncements(data.data);
            } else {
                console.error("Expected an array but got:", data.data);
                SetAnnouncements([]);
            }
        }).catch(error => {
            console.error("Error fetching announcements:", error);
            SetAnnouncements([]);
        });
    }, [trigger]);

    return (
        <div>
            {announcements.map(announcement=><AnnouncementComponent key={announcement.id} announcement={announcement}/>)}
        </div>
    );
};

export default AnnouncementsComponent;