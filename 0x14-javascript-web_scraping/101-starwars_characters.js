#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Function to make a request and return a Promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(`Error fetching data from ${url}: ${error}`);
      } else {
        const data = JSON.parse(body);
        resolve({ name: data.name });
      }
    });
  });
}

// Use Promise.all() to wait for all requests to complete
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const content = JSON.parse(body);
    const characterUrls = content.characters;
    Promise.all(characterUrls.map(makeRequest))
      .then(results => {
        // Results is an array of the objects returned from the makeRequest function
        console.log(results);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
});
