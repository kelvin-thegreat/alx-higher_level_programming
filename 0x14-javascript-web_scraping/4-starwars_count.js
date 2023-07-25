#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

const getNumberOfMoviesWithCharacter = async (apiUrl, characterId) => {
  try {
    const response = await axios.get(apiUrl);
    if (response.status === 200) {
      const films = response.data.results;
      return films.reduce((count, film) => {
        if (film.characters.some((character) => character.includes(`/${characterId}/`))) {
          count++;
        }
        return count;
      }, 0);
    } else {
      console.log('An error occurred. Status code:', response.status);
      return null;
    }
  } catch (error) {
    console.log('An error occurred:', error.message);
    return null;
  }
};

if (!url) {
  console.log('Usage: node movie_counter.js <API_URL>');
} else {
  const characterId = 18;

  getNumberOfMoviesWithCharacter(url, characterId)
    .then((count) => {
      if (count !== null) {
        console.log(`The number of movies where the character 'Wedge Antilles' is present: ${count}`);
      }
    })
    .catch((error) => {
      console.log('An error occurred:', error.message);
    });
}

