#!/usr/bin/node
const lst = process.argv;
if (isNaN(parseInt(lst[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(lst[2]); i++) {
    console.log('C is fun');
  }
}
