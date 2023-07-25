#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('An error occurred while fetching the API:', error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    const printCharacters = (characters, index) => {
      if (index >= characters.length) {
        return;
      }

      request(characters[index], function (charError, charResponse, charBody) {
        if (charError) {
          console.error('An error occurred while fetching character data:', charError);
        } else if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
          printCharacters(characters, index + 1);
        } else {
          console.error('Failed to fetch character data. Status code:', charResponse.statusCode);
        }
      });
    };

    printCharacters(characters, 0);
  } else {
    console.error('Failed to fetch the API. Status code:', response.statusCode);
  }
});

