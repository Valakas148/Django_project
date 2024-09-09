import React from 'react';
import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {useNavigate} from "react-router-dom";

const SignUpPage = () => {
    const {handleSubmit, register} = useForm();
    const navigate = useNavigate()
    const onSubmit = async (formData) => {
        const user = {
            email: formData.email,
            password: formData.password,
            profile: {
                name: formData.name,
                surname: formData.surname,
                age: formData.age,
                phone_number: formData.phone_number
            }
        };
        try {
            await authService.register(user);
            alert('User created Succesful!');
            navigate('')
        } catch (error) {
            console.error('Register error:', error);
            alert('Error register');
        }
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="text" placeholder="Email" {...register('email', {required: true})} />
            <input type="password" placeholder="Password" {...register('password', {required: true})} />

            <input type="text" placeholder="Name" {...register('name', {required: true})} />
            <input type="text" placeholder="Surname" {...register('surname', {required: true})} />
            <input type="number" placeholder="Age" {...register('age', {required: true})} />
            <input type="text" placeholder="Phone Number" {...register('phone_number', {required: true})} />

            <button type="submit">Sign Up</button>
        </form>
    );
};

export default SignUpPage;