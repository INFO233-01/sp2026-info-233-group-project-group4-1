/*
 * Dating App API by Faiza Cutlariwala
 *
 * This API provides random user profiles for browsing in a dating app.
 *
 * Endpoints:

 * - GET /profile : Fetch a random user profile (name, age, gender, bio, interests, picture)
 *
 * To run:
 * 1. npm install
 * 2. npm start
 * Server runs on http://localhost:3000
 *
 * Usage in code:
 * fetch('http://localhost:3000/profile')
 *   .then(res => res.json())
 *   .then(profile => console.log(profile));
 *
 * For testing, open http://localhost:3000 in browser.
 */

const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

// Serve static files (like index.html)
app.use(express.static('.'));

app.get('/profile', async (req, res) => {
  try {
    let name = 'John Doe';
    let age = 25;
    let gender = 'male';
    let bio = 'Love exploring new places and trying new foods!';
    let interests = ['Reading', 'Travel', 'Music'];
    
    try {
      const userResponse = await axios.get('https://randomuser.me/api/');
      const user = userResponse.data.results[0];
      const firstName = user?.name?.first || 'John';
      const lastName = user?.name?.last || 'Doe';
      name = `${firstName} ${lastName}`;
      gender = user?.gender || 'unspecified';
      age = user?.dob?.age || age;
    } catch (userError) {
      console.log('User API failed, using defaults');
    }
    
    try {
      const bioResponse = await axios.get('https://zenquotes.io/api/random');
      bio = bioResponse.data[0]?.q || bio;
    } catch (bioError) {
      console.log('Bio API failed, using default');
    }
    
    try {
      const interestsResponse = await axios.get('https://random-word-api.herokuapp.com/word?number=3');
      interests = interestsResponse.data.map(word => word.charAt(0).toUpperCase() + word.slice(1));
    } catch (interestsError) {
      console.log('Interests API failed, using defaults');
    }
    
    const profile = {
      name: name,
      age: age,
      gender: gender,
      bio: bio,
      interests: interests
    };
    res.json(profile);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to fetch profile' });
  }
});

app.listen(port, () => {
  console.log(`API listening at http://localhost:${port}`);
});