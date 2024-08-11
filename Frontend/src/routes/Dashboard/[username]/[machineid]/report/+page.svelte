<script>
  import { onMount } from 'svelte';
  import { Bar } from 'svelte-chartjs';
  import Chart from 'chart.js/auto';
  import jsPDF from 'jspdf';
  import html2canvas from 'html2canvas';
  import { page } from '$app/stores';

  let parametersData = []; // Array to hold data for each parameter
  let parametersConfig = [
    { name: 'Engine Oil Pressure', thresholds: { min: 25, max: 65 } },
    { name: 'Engine Speed', thresholds: { max: 1800 } },
    { name: 'Engine Temperature', thresholds: { max: 105 } },
    { name: 'Brake Control', thresholds: { min: 1 } },
    { name: 'Transmission Pressure', thresholds: { min: 200, max: 450 } },
    { name: 'Pedal Sensor', thresholds: { max: 4.7 } },
    { name: 'Water Fuel', thresholds: { max: 1800 } },
    { name: 'Fuel Level', thresholds: { min: 1 } },
    { name: 'Fuel Pressure', thresholds: { min: 35, max: 65 } },
    { name: 'Fuel Temperature', thresholds: { max: 400 } },
    { name: 'System Voltage', thresholds: { min: 12.0, max: 15.0 } },
    { name: 'Exhaust Gas Temperature', thresholds: { max: 365 } },
    { name: 'Hydraulic Pump Rate', thresholds: { max: 125 } },
    { name: 'Air Filter Pressure Drop', thresholds: { min: 20 } },
  ];

 
  let userEmail = '';
  let machineName = '';
  let machineId = '';
  let username = '';

  onMount(() => {
    // Extract the path from the URL using $page.url.pathname
    const pathSegments = $page.url.pathname.split('/');
    
    // Assuming path format is: /Dashboard/username/machineId/report
    if (pathSegments.length >= 4) {
      username = pathSegments[2]; // Assuming "Animesh" is in the third position
      machineId = pathSegments[3]; // Assuming "123" is in the fourth position
      console.log(username)

      fetchUserDetails(); // Fetch user details after extracting path parameters
    } else {
      console.error('Invalid URL format. Expected /Dashboard/username/machineId/report');
    }
  });

  const fetchUserDetails = async () => {
    try {
      const response = await fetch('http://localhost:3000/getData');
      if (!response.ok) throw new Error(`Failed to fetch user data. Status: ${response.status}`);

      const allUsers = await response.json();

      const user = allUsers.find(u => u.username === username);
      if (user) {
        const machine = user.machines.find(m => m.id === machineId);
        if (machine) {
          userEmail = user.email;
          machineName = machine.name;
          fetchData(); // Fetch data after finding the correct user and machine
        } else {
          console.error('Machine ID not found for the user');
        }
      } else {
        console.error('User not found');
      }
    } catch (error) {
      console.error('Error fetching user details:', error.message);
    }
  };

  const fetchData = async () => {
    try {
      const response = await fetch(`/api/?type=data&email=${encodeURIComponent(userEmail)}&machine-id=${encodeURIComponent(machineId)}&machine-name=${encodeURIComponent(machineName)}`);
      if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

      const data = await response.json();
      console.log(data);
      if (Array.isArray(data["failure values"]) && Array.isArray(data["parameter values"])) {
        parametersData = parametersConfig.map((param, index) => ({
          name: param.name,
          thresholds: param.thresholds,
          value: data["parameter values"][index],
          failure: data["failure values"][index]
        }));
      } else {
        throw new Error('Invalid data format received');
      }
    } catch (error) {
      console.error('Error fetching data:', error.message);
    }
  };

  const getBarColor = (failure) => {
    if (failure > 0.7) {
      return 'rgba(139, 0, 0, 0.6)';  // Dark Red
    } else if (failure > 0.4) {
      return 'rgba(255, 206, 86, 0.6)';  // Yellow
    } else {
      return 'rgba(75, 192, 192, 1)';  // Green
    }
  };

  const getFailureMessage = (failure) => {
    if (failure > 0.7) {
      return 'Chances of failure is high. Immediate attention required.';
    } else if (failure > 0.4) {
      return 'Failure is medium. Please go to service centre.';
    } else {
      return 'Everything is fine.';
    }
  };

 

  const downloadPDF = () => {
    const pdf = new jsPDF('p', 'mm', 'a4');
    const container = document.querySelector('#pdf-container');

    html2canvas(container).then(canvas => {
      const imgData = canvas.toDataURL('image/png');
      const imgWidth = 190; // A4 width
      const pageHeight = 295; // A4 height
      const imgHeight = (canvas.height * imgWidth) / canvas.width;
      let heightLeft = imgHeight;
      let position = 10;

      pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
      heightLeft -= pageHeight;

      while (heightLeft >= 0) {
        position = heightLeft - imgHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;
      }

      pdf.save('charts.pdf');
    });
  };
</script>

<div id="pdf-container">
  <header>
    <h1>Vehicle Health Report</h1>
    <p>A detailed analysis of your vehicle's key parameters.</p>
  </header>

  <section>
    {#each parametersData as { name, thresholds, value, failure }}
      {#if value !== undefined && failure !== undefined}
        <div class="chart-container">
          <h3>{name}</h3>
          <Bar
            {Chart}
            options={{
              responsive: true,
              plugins: {
                legend: { display: false },
                title: {
                  display: true,
                  text: `${name} Values`
                }
              },
              scales: {
                x: {
                  beginAtZero: true,
                },
                y: {
                  beginAtZero: true,
                  min: thresholds.min || 0,
                  max: thresholds.max || Math.max(...parametersData.map(p => p.value)) * 1.1,
                  title: {
                    display: true,
                    text: 'Value'
                  }
                }
              }
            }}
            data={{
              labels: [name],
              datasets: [{
                label: name,
                data: [value],
                backgroundColor: [getBarColor(failure)],
                borderColor: [getBarColor(failure)],
                borderWidth: 1
              }]
            }}
          />
          <p class="status-message">{getFailureMessage(failure)}</p>
        </div>
      {:else}
        <p>Loading data...</p>
      {/if}
    {/each}
  </section>

  <footer>
    <button on:click={downloadPDF}>Download as PDF</button>
  </footer>
</div>

<style>
  #pdf-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  header {
    text-align: center;
    margin-bottom: 30px;
  }

  header h1 {
    font-size: 2em;
    margin-bottom: 10px;
    color: #333;
  }

  header p {
    font-size: 1.2em;
    color: #666;
  }

  section {
    margin-bottom: 40px;
  }

  .chart-container {
    background: white;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
  }

  h3 {
    text-align: center;
    margin-bottom: 10px;
    font-size: 1.2em;
    color: #444;
  }

  .status-message {
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
    color: #333;
  }

  footer {
    text-align: center;
    margin-top: 20px;
  }

  footer button {
    background-color: #007BFF;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  footer button:hover {
    background-color: #0056b3;
  }
</style>
