<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    let showModal = false;
    let machineId = '';
    let machineName = '';
    let selectedUserIndex = null;

    let loggedInUser = null;
    let allUsers = [];

    // Fetch users from the backend
    onMount(async () => {
        await fetchUsers();
    });

    async function fetchUsers() {
        try {
            const response = await fetch('http://localhost:3000/users');
            const data = await response.json();
            allUsers = data;

            // Extract the logged-in user's username from the URL
            $: if ($page) {
                const loggedInUsername = $page.params.username;

                // Find the logged-in user based on the username
                loggedInUser = allUsers.find(user => user.username === loggedInUsername);
            }
        } catch (error) {
            console.error('Error fetching users:', error);
            alert('Failed to load data');
        }
    }

    function openModal() {
        showModal = true;
    }

    function closeModal() {
        showModal = false;
        machineId = '';
        machineName = '';
    }

    async function addMachine() {
        if (machineId && machineName && loggedInUser) {
            const username = loggedInUser.username;

            try {
                const response = await fetch(`http://localhost:3000/users/${username}/machines`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ id: machineId, name: machineName })
                });

                const result = await response.json();

                if (result.success) {
                    // Fetch updated users
                    await fetchUsers();
                    closeModal();
                } else {
                    alert('Failed to save machine');
                }
            } catch (error) {
                console.error('Error adding machine:', error);
                alert('An error occurred while saving data');
            }
        } else {
            alert('Please enter both machine ID and machine name');
        }
    }
</script>

<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f4f8;
        margin: 0;
        padding: 0;
    }

    /* Navbar Styling */
    .navbar {
        background-color: #333;
        color: white;
        padding: 15px;
        text-align: center;
        position: sticky;
        top: 0;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar a {
        color: white;
        text-decoration: none;
        margin-left: 20px;
        font-size: 1.2rem;
        transition: color 0.2s;
    }

    .navbar a:hover {
        color: #ffcd11;
    }

    .content {
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 100vh;
    }

    h2, h3 {
        margin-top: 0;
        color: #333;
    }
  
    p {
        color: #666;
    }
  
    /* Button styling */
    button {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-right: 10px;
        transition: background-color 0.2s;
    }
  
    button:hover {
        background-color: #0056b3;
    }
  
    /* Machine card styling */
    .machine-card {
        background: #fff;
        padding: 20px;
        margin: 15px 0;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.2s, transform 0.2s;
        text-decoration: none;
        color: inherit;
        display: block;
        width: 100%;
        max-width: 400px;
    }

    .machine-card:hover {
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        transform: translateY(-5px);
    }

    .machine-card h3 {
        margin: 0 0 5px;
        color: #343a40;
    }

    .machine-card p {
        margin: 0;
        color: #6c757d;
    }

    /* Modal styling */
    .modal-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
    }

    .modal {
        display: block;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        z-index: 1000;
        width: 100%;
        max-width: 400px;
        animation: fadeIn 0.3s ease-in-out;
    }

    /* Input field styling */
    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 1rem;
    }
  
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translate(-50%, -45%); }
        to { opacity: 1; transform: translate(-50%, -50%); }
    }

    @keyframes fadeInBackground {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .Logo{
        padding-left: 100px;
        width: 75px;
    }
</style>

<body>
    <!-- Navbar -->
    <div class="navbar">
        <img class="Logo" src="/img/CATLogo.jpg" alt="Logo">
        <div>
            <a href="/docs">Docs</a>
            <a href="/">LogOut</a>
        </div>
        
            
    </div>

    <!-- Content -->
    <div class="content">
        {#if loggedInUser}
            <h2>Welcome, {loggedInUser.username}</h2>

            <button on:click={openModal}>Add Machine</button>
        

            <h2 style="padding-top:25px">Your Machines</h2>

            {#each loggedInUser.machines as machine (machine.id)}
                <a href="/Dashboard/{loggedInUser.username}/{machine.id}/report" class="machine-card">
                    <h3>{machine.name}</h3>
                    <p>ID: {machine.id}</p>
                </a>
            {/each}
        {/if}
    </div>

    <!-- Modal for machine details input -->
    {#if showModal}
        <div class="modal-background" on:click={closeModal}></div>
        <div class="modal" role="dialog" aria-labelledby="modal-title">
            <h2 id="modal-title">Add Machine</h2>
            <label>
                Machine ID:
                <input type="text" bind:value={machineId} />
            </label>
            <label>
                Machine Name:
                <input type="text" bind:value={machineName} />
            </label>
            <div>
                <button on:click={addMachine}>Submit</button>
                <button on:click={closeModal}>Cancel</button>
            </div>
        </div>
    {/if}
</body>