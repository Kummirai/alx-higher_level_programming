#!/usr/bin/node
// Script that concats 2 files
let file = require('fs');
file.readFile(process.argv[2], function (error, data) {
  if (error) {
    return;
  }
  file.appendFile(process.argv[4], data, {});
});
file.readFile(process.argv[3], function (error, data) {
  if (error) {
    return;
  }
  file.appendFile(process.argv[4], data, {});
});
