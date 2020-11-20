/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function (arr) {
  if (arr.length == 0) {
    return [];
  }
  let r = 1;
  let m = {};
  let p = Math.min(...arr) - 1;
  let arr2 = [...arr].sort((a, b) => a - b);
  arr2.map((x) => {
    if (x > p) {
      m[x] = r;
      r++;
      p = x;
    }
  });
  return arr.map((x) => m[x]);
};

var arrayRankTransform2 = function (arr) {
  var sorted = Array.from(new Set(arr)).sort((a, b) => a - b);
  return arr.map((x) => sorted.indexOf(x) + 1);
};

var arrayRankTransform3 = function (arr) {
  var dic = new Map(
    Array.from(new Set(arr))
      .sort((a, b) => a - b)
      .map((x, i) => [x, i + 1])
  );
  return arr.map((x) => dic.get(x));
};

//console.log(arrayRankTransform([40, 10, 30, 20, 30]));
console.log(arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]));
