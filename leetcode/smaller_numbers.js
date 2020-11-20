/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
  let n = [];
  let t = 0;
  for (let x = 0; x < nums.length; x++) {
    t = 0;
    for (let y = 0; y < nums.length; y++) {
      if (nums[y] < nums[x]) {
        t++;
      }
    }
    n.push(t);
  }
  return n;
};

console.log(smallerNumbersThanCurrent([8, 1, 2, 2, 3]));
