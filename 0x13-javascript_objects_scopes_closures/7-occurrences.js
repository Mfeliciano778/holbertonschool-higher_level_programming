#!/usr/bin/node
module.exports.nbOccurences = function (list, num) {
  let occur = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === num) {
      occur = occur + 1;
    }
  }
  return occur;
};
