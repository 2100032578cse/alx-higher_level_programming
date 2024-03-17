#!/usr/bin/node
exports.esrever = function (list) {
  const lst = [];
  let i = list.length - 1;
  while (i >= 0) {
    lst.push(list[i]);
    i--;
  }
  return lst;
};
