#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('An error occurred while fetching the URL:', error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.error('An error occurred while writing to the file:', err);
      }
    });
  } else {
    console.error('Failed to fetch the URL. Status code:', response.statusCode);
  }
});

