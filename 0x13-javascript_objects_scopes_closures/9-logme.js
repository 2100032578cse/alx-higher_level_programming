#!/usr/bin/node
const c = 0;
exports.logMe = function (item) {
  console.log('${c++}: ${item}');
};
