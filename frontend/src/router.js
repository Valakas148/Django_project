import {createBrowserRouter} from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import LoginPage from "./pages/LoginPage";
import AnnouncementsPage from "./pages/AnnouncementsPage";
import AnnouncementFormCreateComponent from "./components/Announcements/AnnouncementFormCreateComponent";
import SignUpPage from "./pages/SignUpPage";
import CarAdminPage from "./pages/CarAdminPage";

const router  = createBrowserRouter(
    [
        {
            path:'', element:<MainLayout/>, children:[
                {
                    path: '', element: <AnnouncementsPage/>, index: true
                },
                {
                    path: 'announcements', element:<AnnouncementFormCreateComponent/>
                },
                {
                    path: 'login', element: <LoginPage/>
                },
                {
                    path: 'sign-up', element: <SignUpPage/>
                },
                {
                    path: 'cars', element: <CarAdminPage/>
                }
            ]
        }
    ]
)

export{
    router
}