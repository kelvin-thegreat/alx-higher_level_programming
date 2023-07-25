#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];
const characterId = 18;

request(apiURL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const moviesWithWedge = data.results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(`${moviesWithWedge.length}`);
  } else {
    console.log(`An error occurred. Status code: ${response.statusCode}`);
  }
});

