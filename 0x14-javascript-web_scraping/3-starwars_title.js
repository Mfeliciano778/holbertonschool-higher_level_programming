#!/usr/bin/node
const req = require('request');
const arg = process.argv[2];
const starWars = 'https://swapi-api.hbtn.io/api/films/';

req.get({ url: starWars + arg }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
