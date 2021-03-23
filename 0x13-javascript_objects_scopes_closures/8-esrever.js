#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let index = list.length; index > 0; index--) {
    newlist.push([list[index - 1]]);
  }
  return newlist;
};
