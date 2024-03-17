#!/usr/bin/node
const lst = process.argv;
const ch = 'X';
if (isNaN(parseInt(lst[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(lst[2]); i++) {
    console.log(ch.repeat(parseInt(lst[2])));
  }
}
