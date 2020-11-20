/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
  return Math.max(
    ...nums
      .toString()
      .replace(/,/g, "")
      .split("0")
      .map((l) => l.length)
  );
};

var findMaxConsecutiveOnes2 = function (nums) {
  return nums
    .join("")
    .split("0")
    .reduce((max, ones) => Math.max(max, ones.length), 0);
};

var findMaxConsecutiveOnes3 = function (nums) {
  let str = nums.join(""),
    max = nums.length + 1;
  while (!~str.indexOf("1".repeat(--max)) && max);
  return max;
};

console.log(findMaxConsecutiveOnes3([1, 1, 0, 1, 1, 1]));
console.log(findMaxConsecutiveOnes3([0, 0, 0, 0, 0, 0]));
