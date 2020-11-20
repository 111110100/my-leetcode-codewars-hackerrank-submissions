/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function (mat, k) {
  //let m = mat.map((n, index) => {
  //  return [index, n.reduce((a, b) => a + b, 0)];
  //});
  //return m.sort((x, y) => x[1] - y[1]).map((x) => x[0]);
  //return mat.sort(
  //  (a, b) => b.reduce((x, y) => x + y, 0) - a.reduce((x, y) => x + y, 0)
  //);
  return mat
    .map((n, index) => [index, n.reduce((a, b) => a + b, 0)])
    .sort((a, b) => a[1] - b[1])
    .map((n) => n[0])
    .slice(0, k);
};

console.log(
  kWeakestRows(
    [
      [1, 1, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1],
    ],
    4
  )
);
