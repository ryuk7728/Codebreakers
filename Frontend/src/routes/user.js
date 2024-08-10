
import { writable } from 'svelte/store';

export const users = writable([{
    username:"animesh",
    email:"a@gmail.com",
    password:"animesh",
    machines:[]
}]);
