import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Login from "./components/login/Login";
import SignUpCustomer from "./components/signup/Signup_customer";
import SelectSignupRole from "./components/signup/SelectSignupRole";
import SignUpArtisan from "./components/signup/Signup_artisan";

const routes = createBrowserRouter( [
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "/signup",
    element: <SelectSignupRole/>,
  },
  {
    path: "/signup_customer",
    element: <SignUpCustomer />,
  },
  {
    path: "/signup_artisan",
    element: <SignUpArtisan />,
  }
])


export default function App() {
  return <RouterProvider router={routes} />;
}