
<script>
    import { users } from '../user.js';
    import { goto } from '$app/navigation';
    import { get } from 'svelte/store';

    let email = '';
    let password = '';
    let errorMessage = '';

    const handleLogin = () => {
        const allUsers = get(users);  
        const user = allUsers.find(u => u.email === email && u.password === password);

        if (user) {
            goto(`/Dashboard/${user.name}`);
        } else {
            errorMessage = 'Invalid email or password';
        }
    };
</script>

<style>
    .error {
        color: red;
        margin-top: 10px;
    }
</style>

<form on:submit|preventDefault={handleLogin}>
    <label>
        Email:
        <input type="email" bind:value={email} placeholder="Enter your email" />
    </label>

    <label>
        Password:
        <input type="password" bind:value={password} placeholder="Enter your password" />
    </label>

    <button type="submit">Login</button>

    {#if errorMessage}
        <p class="error">{errorMessage}</p>
    {/if}
</form>
