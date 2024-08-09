<!-- src/Signup.svelte -->
<script>
    import { users } from '../user.js';
    import { goto } from '$app/navigation';

    let username = '';
    let email = '';
    let password = '';

    const handleSignup = () => {
        if (username && email && password) {
            users.update(currentUsers => {
                return [...currentUsers, { name, email, password }];
            });

            // Clear the input fields after signup
            username = '';
            email = '';
            password = '';
            goto('/');
        } else {
            alert("Please fill in all fields.");
        }
    };
</script>

<style>
    form {
        max-width: 300px;
        margin: auto;
        padding: 2rem;
        border: 1px solid #ccc;
        border-radius: 10px;
    }

    label {
        display: block;
        margin-bottom: 0.5rem;
    }

    input {
        width: 100%;
        padding: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    button {
        padding: 0.5rem 1rem;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }

    .container{
        background-color: red;
    }
</style>

<form on:submit|preventDefault={handleSignup}>
    <div class="container">
    <label>
        Name:
        <input type="text" bind:value={username} placeholder="Enter your name" />
    </label>

    <label>
        Email:
        <input type="email" bind:value={email} placeholder="Enter your email" />
    </label>

    <label>
        Password:
        <input type="password" bind:value={password} placeholder="Enter your password" />
    </label>

    <button type="submit">Sign Up</button>
</div>
</form>
