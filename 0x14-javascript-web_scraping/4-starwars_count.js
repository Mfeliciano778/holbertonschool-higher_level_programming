#!/usr/bin/node
const req = require('request');
const starWars = process.argv[2];

req.get({ url: starWars }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    let num = 0;
    for (const movies of json.results) {
      for (const id of movies.characters) {
        if (id.includes('18')) {
          num += 1;
        }
      }
    }
    console.log(num);
  }
});
