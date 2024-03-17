#!/usr/bin/node
const list = require('./100-data.js').list;
const lst = list.map((item, index) => item * index);
console.log(list);
console.log(lst);
