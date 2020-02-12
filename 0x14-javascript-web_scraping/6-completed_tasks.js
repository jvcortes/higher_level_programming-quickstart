#!/usr/bin/node
// Copies a HTTP GET response body to a file.
const request = require('request');

request(process.argv[2],
  function (err, response, body) {
    if (err) {
      console.error(err);
    } else {
      let ids = [];
      const todos = JSON.parse(body);
      const count = {};
      for (const todo of todos) {
        ids.push(todo.userId);
      }
      ids = [...new Set(ids)];
      for (const id of ids) {
        count[id] = todos.filter(
          todo => todo.userId === id && todo.completed).length;
      }
      console.log(count);
    }
  }
);
