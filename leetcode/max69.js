/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
  return num.toString().replace("6", "9");
};

console.log(maximum69Number(9669));
console.log(maximum69Number(9996));
console.log(maximum69Number(9999));
console.log(maximum69Number(666));
