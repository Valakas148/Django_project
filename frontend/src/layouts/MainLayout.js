import React from 'react';
import {NavLink, Outlet} from "react-router-dom";
import LoginPage from "../pages/LoginPage";
import SignUpPage from "../pages/SignUpPage";
import AnnouncementsPage from "../pages/AnnouncementsPage";

const MainLayout = () => {

    


    return (
        <div>
            {/*<h3>Login</h3>*/}
            {/*<LoginPage/>*/}
            {/*<h2>Or create Account</h2>*/}
            {/*<SignUpPage/>*/}
            <NavLink to={''}>Main</NavLink>
            <br/>
            <NavLink to={'login'}>Login</NavLink>
            <br/>
            <NavLink to={'sign-up'}>Sign-up</NavLink>
            <br/>
            <NavLink to={'announcements'}>Create Announcement</NavLink>
            <br/>
            <NavLink to={'cars'}>Admin Car Page</NavLink>
            <br/>
            <hr/>
            <Outlet/>
        </div>
    );
};

export default MainLayout;