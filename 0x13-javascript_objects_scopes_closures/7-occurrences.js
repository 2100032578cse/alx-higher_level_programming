#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const outp = list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
  return outp;
};
