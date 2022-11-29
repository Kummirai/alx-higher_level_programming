#!/usr/bin/node
// Script that prints using an array and a loop
myVar = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let txt = " ";
myVar.forEach(myFunction);
console.log(txt);

function myFunction(value, index, array) { txt += value;}
