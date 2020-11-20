/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function (nums) {
  let goodPairs = 0;
  for (let x = 0; x < nums.length; x++) {
    for (let y = x + 1; y < nums.length; y++) {
      if (x < y && nums[x] == nums[y]) {
        goodPairs++;
      }
    }
  }
  return goodPairs;
};

console.log(numIdenticalPairs([1, 2, 3, 1, 1, 3]));
