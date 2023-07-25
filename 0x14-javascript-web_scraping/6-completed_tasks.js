#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    });

    for (const userId in completedTasksByUser) {
      console.log(`'${userId}' : ${completedTasksByUser[userId]}`);
    }
  } else {
    console.error(`Failed to fetch the API. Status code: ${response.statusCode}`);
  }
});

