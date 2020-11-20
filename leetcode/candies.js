/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  let maxCandies = Math.max(...candies);
  return candies.map((candy) => candy + extraCandies >= maxCandies);
};

console.log(kidsWithCandies([2, 3, 5, 1, 3], 3));
