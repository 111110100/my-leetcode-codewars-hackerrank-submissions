/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function (grid) {
  return [].concat.apply([], grid).filter((n) => n < 0).length;
};

console.log(
  countNegatives([
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3],
  ])
);
