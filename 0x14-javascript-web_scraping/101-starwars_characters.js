#!/usr/bin/node

const request = require('request');
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = parseInt(process.argv[2], 10);
let characterUrls = [];

request(filmUrl, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const films = resp.results;
    for (let i = 0; i < films.length; i++) {
      if (films[i].episode_id === movieId) {
        characterUrls = films[i].characters;
        break;
      }
    }
    for (let j = 0; j < characterUrls.length; j++) {
      request(characterUrls[j], function (err, response, body) {
        if (err == null) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    }
  }
});
