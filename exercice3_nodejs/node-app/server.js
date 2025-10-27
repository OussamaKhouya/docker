const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Bienvenue sur la page d\'accueil !');
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'OK' });
});

app.get('/api/info', (req, res) => {
  res.json({ environment: process.env.NODE_ENV || 'dev', nodeVersion: process.version });
});

app.get('/api/time', (req, res) => {
  res.json({ time: new Date().toISOString() });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Serveur démarré sur le port ${PORT}`);
});