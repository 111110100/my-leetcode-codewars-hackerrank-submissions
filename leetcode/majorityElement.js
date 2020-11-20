/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  let count = {};
  let highest = 0;
  let t = 0;
  nums.forEach((n) => (count[n] = (count[n] || 0) + 1));
  for (const [k, v] of Object.entries(count)) {
    if (t < v) {
      highest = k;
      t = v;
    }
  }
  return highest;
};

var majorityElement2 = function (nums) {
  var obj = {};

  for (var i = 0; i < nums.length; i++) {
    obj[nums[i]] = obj[nums[i]] + 1 || 1;
    if (obj[nums[i]] > nums.length / 2) return nums[i];
  }
};

var majorityElement3 = function (nums) {
  // sort the array and the middle is the majority
  nums.sort((a, b) => a - b);
  return nums[Math.floor(nums.length / 2)];
};

console.log(majorityElement3([2, 2, 1, 1, 1, 2, 2]));
