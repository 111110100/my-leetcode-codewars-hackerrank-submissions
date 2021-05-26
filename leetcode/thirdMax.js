/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function (nums) {
  let n = new Set(nums.sort((a, b) => a - b));
  if (n.size < 3) {
    return Math.max(...n);
  }
  return Array.from(n)[n.size - 3];
};

console.log(thirdMax([2, 1]));
console.log(thirdMax([2, 2, 3, 1]));
console.log(thirdMax([2, 2, 3, 1, 3, 3, 5, 5, 6, 6]));
