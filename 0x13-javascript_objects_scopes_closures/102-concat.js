#!/usr/bin/node
const fs = require('fs');
const d = fs.readFileSync(process.argv[2], 'utf8');
const e = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], d + e);
