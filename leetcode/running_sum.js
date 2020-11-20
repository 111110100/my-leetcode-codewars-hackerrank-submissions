/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
  let ans = [];
  for (let i = 1; i <= nums.length; i++) {
    ans.push(nums.slice(0, i).reduce((x, y) => x + y, 0));
  }
  return ans;
};

console.log(runningSum([1, 2, 3, 4]));

/**

    return nums.reduce((a,c,i,arr) => arr[i] += a)

 */
