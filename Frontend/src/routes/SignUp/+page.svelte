<!-- src/Signup.svelte -->
<script>
    import { goto } from '$app/navigation';

    let username = '';
    let email = '';
    let password = '';

    const handleSignup = async () => {
        if (username && email && password) {
            const newUser = { username, email, password, machines: [] };

            try {
                const response = await fetch('http://localhost:3000/addUser', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(newUser),
                });

                const result = await response.json();

                if (result.success) {
                    // Clear the input fields after successful signup
                    username = '';
                    email = '';
                    password = '';
                    goto('/');
                } else {
                    alert('Failed to sign up. Please try again.');
                }
            } catch (error) {
                console.error('Error during signup:', error);
                alert('An error occurred during signup. Please try again.');
            }
        } else {
            alert("Please fill in all fields.");
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
        justify-content: center;
        height: 100vh;
        position: relative;
    }

    .container {
        display: flex;
        align-items: center;
        background-color: white;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        overflow: hidden;
        position: relative;
        z-index: 1;
    }

    .left-side {
        background-color: #FFCD11;
        width: 31%; /* Similar width to login page */
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 20px;
        margin-left: 25px;
        height: 729px;
    }

    .left-side .logo img {
        max-width: 80%;
        height: auto;
        margin-left: 42px;
    }

    .left-side .text {
        font-size: 2rem; /* Slightly increased font size */
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }

    .right-side {
        width: 30%; /* Similar width to login page */
        padding: 40px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        position: absolute;
        left: 526px;
    }

    form {
        display: flex;
        flex-direction: column;
    }

    form label {
        display: block;
        font-size: 1.1rem;
        margin-bottom: 10px;
    }

    form input {
        width: 100%;
        padding: 10px;
        margin-top: 5px;
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 1rem;
    }

    form button {
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

    form button:hover {
        background-color: #555;
    }

    .signup-info {
        text-align: center;
        margin-top: 20px;
        font-size: 1rem;
    }

    .signup-info a {
        color: #FFCD11;
        text-decoration: none;
        font-weight: bold;
    }

    .signup-info a:hover {
        text-decoration: underline;
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
        <div class="right-side">
            <form on:submit|preventDefault={handleSignup}>
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

                <p class="signup-info">Already have an account? <a href="/">Log In</a></p>
            </form>
        </div>
        <div id="right-side"></div>
    </div>
</body>