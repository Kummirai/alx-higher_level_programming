#!/usr/bin/node
// Function that prints the number of arguments already printed and the new argument value
let funcCalls = 0;
exports.logMe = function (item) {
  console.log(`${funcCalls}: ${item}`);
  funcCalls++;
};
