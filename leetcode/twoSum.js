/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let d = {};
  for (const [i, v] of numbers.entries()) {
    let m = target - v;
    //if (m in d) {
    if (d.hasOwnProperty(m)) {
      return [d[m], i + 1];
    } else {
      d[v] = i + 1;
    }
  }
};

console.log(twoSum([2, 7, 11, 15], 9));
