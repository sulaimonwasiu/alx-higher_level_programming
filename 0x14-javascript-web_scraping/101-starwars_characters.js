#!/usr/bin/node
// Assuming you're running this script with Node.js

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Import the 'request' module
const request = require('request');

// Set the API endpoint URL
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make the GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    // Parse the response body as JSON
    const movie = JSON.parse(body);
    // Get the list of characters
    const characters = movie.characters;

    // Print each character name
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error(`Error fetching character: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Error fetching movie: ${response.statusCode}`);
  }
});
