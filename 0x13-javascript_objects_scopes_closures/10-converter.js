#!/usr/bin/node
exports.converter = function (base) {
  return outp => outp.toString(base);
};
