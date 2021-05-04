#!/usr/bin/node
const req = require('request');
const starWars = process.argv[2];

req.get({ url: starWars }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const newDict = {};
    const json = JSON.parse(body);
    for (const ppl of json) {
      if (ppl.completed === true) {
        if (newDict[ppl.userId] === undefined) {
          newDict[ppl.userId] = 1;
        } else {
          newDict[ppl.userId] += 1;
        }
      }
    }
    console.log(newDict);
  }
});
