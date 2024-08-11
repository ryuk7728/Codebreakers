<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';

    let email = '';
    let password = '';
    let errorMessage = '';

    // Function to handle login
    const handleLogin = async () => {
        try {
            // Fetch user data from the backend
            const response = await fetch('http://localhost:3000/getData');
            const allUsers = await response.json();

            // Check if the email and password match
            const user = allUsers.find(u => u.email === email && u.password === password);
            console.log(user);

            if (user) {
                goto(`/Dashboard/${user.username}`);
            } else {
                errorMessage = 'Invalid email or password';
            }
        } catch (error) {
            console.error('Error during login:', error);
            errorMessage = 'An error occurred during login. Please try again.';
        }
    };
</script>

<style>
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }

    body {
        background-color: white;
        font-family: 'Arial', sans-serif;
        color: #333;
    }

    .container {
        display: flex;
        min-height: 100vh;
        align-items: center;
        /* justify-content: center; */
    }

    .left-side {
        background-color: #FFCD11;
        width: 31%; /* Increase width to cover more of the left side */
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 20px;
        margin-left: 25px;
    }

    .left-side .logo img {
        max-width: 80%; /* Adjusted to ensure the image fits nicely within the wider column */
        height: auto;
        margin-left: 42px;
    }

    .left-side .text {
        font-size: 2rem; /* Slightly increased font size for better balance */
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }

    .right {
        background-color: white;
        padding: 40px;
        width: 30%;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        position: absolute;
        left: 526px;
    }

    .right .form .heading {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 30px;
    }

    .right .form label {
        display: block;
        font-size: 1.1rem;
        margin-bottom: 10px;
    }

    .right .form input {
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 1rem;
    }

    .right .form .btn {
        width: 100%;
        padding: 12px;
        font-size: 1.2rem;
        color: white;
        background-color: #333;
        border-radius: 5px;
        border: none;
        margin-top: 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .right .form .btn:hover {
        background-color: #555;
    }

    .right .form p.sign {
        text-align: center;
        margin-top: 20px;
        font-size: 1rem;
    }

    .right .form p.sign a {
        color: #FFCD11;
        text-decoration: none;
        font-weight: bold;
    }

    .right .form p.sign a:hover {
        text-decoration: underline;
    }

    .right .form .error {
        color: red;
        font-size: 0.9rem;
        margin-top: 15px;
        text-align: center;
    }

    #right-side {
        height: 100vh;
        width: 34%;
        background-image: url("/img/constructionman.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        border-radius: 0 8px 8px 0;
        position: absolute;
        right: 0px;
    }
</style>

<body>
    <div class="container">
        <div class="left-side">
            <div class="logo">
                <img src="/img/CATLogo.jpg" alt="logo">
            </div>
            <div class="text">
                <p>"<br>BUILDING BETTER<br>"</p>
            </div>
        </div>

        <div class="right">
            <div class="form" id="form">
                <p class="heading">LOG IN</p>

                <form on:submit|preventDefault="{handleLogin}" class="form-log">
                    <label>
                        EMAIL
                        <input type="email" bind:value="{email}" placeholder="Enter your email" />
                    </label>

                    <label>
                        PASSWORD
                        <input type="password" bind:value="{password}" placeholder="Enter your password" />
                    </label>

                    <button type="submit" class="btn">Login</button>

                    {#if errorMessage}
                        <p class="error">{errorMessage}</p>
                    {/if}
                </form>
                <p class="sign">Don't have an account? <a href="/SignUp">Sign Up</a></p>
            </div>
        </div>

        <div id="right-side"></div>
    </div>
</body>