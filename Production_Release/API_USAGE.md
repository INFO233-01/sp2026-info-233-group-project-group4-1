# Dating App API Usage Guide

## Overview
This API provides random user profiles for a dating application. It fetches data from free online services to generate profiles with name, age, gender, bio, and interests.

## Endpoints

### GET /profile
Fetches a random user profile.

**Response:**
```json
{
  "name": "Neha Bhoja",
  "age": 79,
  "gender": "female",
  "bio": "Normality is a paved road: It's comfortable to walk, but no flowers grow on it.",
  "interests": ["Naphthylamine", "Auxetics", "Hearths"]
}
```

## How to Run
1. Install dependencies: `npm install`
2. Start the server: `npm start`
3. Open `http://localhost:3000` in a browser to load the front-end and test the API

## How to Use in Your Code
### JavaScript (using fetch)
```javascript
fetch('/profile')
  .then(response => response.json())
  .then(profile => {
    console.log(profile.name);
    console.log(profile.bio);
    // etc.
  });
```

### JavaScript (using axios)
```javascript
const axios = require('axios');

axios.get('/profile')
  .then(response => {
    const profile = response.data;
    // use profile data
  });
```

## Testing
- Open `http://localhost:3000` in a browser to use the front-end
- Use `http://localhost:3000/profile` to get a sample profile JSON
- The front-end in `index.html` displays profile data and has like/pass buttons (test only)

## Notes
- Names, age, and gender are fetched from `https://randomuser.me/api/`
- Bios are fetched from `https://zenquotes.io/api/random`
- Interests are fetched from `https://random-word-api.herokuapp.com/word?number=3`
- If any external API fails, the server falls back to default values