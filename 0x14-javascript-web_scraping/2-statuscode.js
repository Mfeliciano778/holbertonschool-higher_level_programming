#!/usr/bin/node
const req = require('request');
const arg = process.argv[2];

req.get({ url: arg }, function (err, res) {
  if (err) {
    console.log('code: ' + res.statusCode);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
