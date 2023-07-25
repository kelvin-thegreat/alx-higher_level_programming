#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(`${movieData.title}`);
  } else {
    console.log(`An error occurred. Status code: ${response.statusCode}`);
  }
});

