import React from 'react';
import AnnouncementFormCreateComponent from "../components/Announcements/AnnouncementFormCreateComponent";
import AnnouncementsComponent from "../components/Announcements/AnnouncementsComponent";

const AnnouncementsPage = () => {
    return (
        <div>
            {/*<h1>Create your Announcement</h1>*/}
            {/*<AnnouncementFormCreateComponent/>*/}

            <hr/>
            <h3>All Announcements</h3>
            <AnnouncementsComponent/>
            <hr/>
        </div>
    );
};

export default AnnouncementsPage;