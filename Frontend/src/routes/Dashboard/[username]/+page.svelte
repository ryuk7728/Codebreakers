<script>
    import { onMount } from 'svelte';
  
    let showModal = false;
    let machineId = '';
    let machineName = '';
    let selectedUserIndex = null;
  
    let allUsers = [];
  
    // Fetch users from the backend
    onMount(async () => {
        await fetchUsers();
    });
  
    async function fetchUsers() {
        try {
            const response = await fetch('http://localhost:3000/users');
            const data = await response.json();
            allUsers = data;  // Directly assign the fetched data to allUsers
        } catch (error) {
            console.error('Error fetching users:', error);
            alert('Failed to load data');
        }
    }
  
    function openModal(userIndex) {
        selectedUserIndex = userIndex;
        showModal = true;
    }
  
    function closeModal() {
        showModal = false;
        machineId = '';
        machineName = '';
    }
  
    async function addMachine() {
        if (machineId && machineName && selectedUserIndex !== null) {
            const username = allUsers[selectedUserIndex].username;
  
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
    .modal {
        display: block;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 20px;
        border: 1px solid #ccc;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
  
    .modal-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
    }
  
    .card {
        background: #f9f9f9;
        padding: 15px;
        margin: 10px;
        border-radius: 5px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    }
  </style>
  
  {#if allUsers.length > 0}
    {#each allUsers as user, index}
        <div class="card">
            <h2>{user.username}</h2>
            <button on:click={() => openModal(index)}>Add Machine</button>
  
            <!-- Displaying each machine as a card -->
            <div>
                {#each user.machines as machine (machine.id)}
                    <div class="card">
                        <h3>{machine.name}</h3>
                        <p>ID: {machine.id}</p>
                    </div>
                {/each}
            </div>
        </div>
    {/each}
  {/if}
  
  <!-- Modal for machine details input -->
  {#if showModal && selectedUserIndex !== null}
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
        <button on:click={addMachine}>Submit</button>
        <button on:click={closeModal}>Cancel</button>
    </div>
  {/if}
  