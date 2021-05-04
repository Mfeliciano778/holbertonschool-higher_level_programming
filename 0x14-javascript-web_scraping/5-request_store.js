#!/usr/bin/node
const fs = require('fs');
const req = require('request');

const contentUrl = process.argv[2];
const filename = process.argv[3];

req.get({ url: contentUrl }, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
