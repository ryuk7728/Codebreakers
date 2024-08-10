const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
const PORT = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Path to the JSON file
const FilePath = path.join(__dirname, 'data', 'users.json');

// Route to fetch data
app.get('/getData', (req, res) => {
  fs.readFile(FilePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading user data:', err);
      return res.status(500).json({ success: false, message: 'Failed to load data' });
    }
    res.json(JSON.parse(data));
  });
});

app.get('/users', (req, res) => {
  fs.readFile(FilePath, (err, data) => {
    if (err) return res.status(500).send(err.message);
    res.json(JSON.parse(data));
  });
});

// Route to add a new user
app.post('/addUser', (req, res) => {
  const { username, email, password, machines = [] } = req.body; // Default machines to an empty array

  if (!username || !email || !password) {
    return res.status(400).send('Missing required fields');
  }

  fs.readFile(FilePath, (err, data) => {
    if (err) return res.status(500).send(err.message);

    let users = JSON.parse(data);

    // Check if the user already exists
    const existingUser = users.find(u => u.email === email);
    if (existingUser) return res.status(400).send('User already exists');

    // Add new user to the list
    users.push({ username, email, password, machines });

    fs.writeFile(FilePath, JSON.stringify(users, null, 2), (err) => {
      if (err) return res.status(500).send(err.message);
      res.json({ success: true });
    });
  });
});

// Add a machine to a specific user
app.post('/users/:username/machines', (req, res) => {
  const { username } = req.params;
  const { id, name } = req.body;

  fs.readFile(FilePath, (err, data) => {
    if (err) return res.status(500).send(err.message);

    let users = JSON.parse(data);
    const user = users.find(u => u.username === username);

    if (!user) return res.status(404).send('User not found');

    user.machines.push({ id, name });

    fs.writeFile(FilePath, JSON.stringify(users, null, 2), (err) => {
      if (err) return res.status(500).send(err.message);
      res.json({ success: true });
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
