/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function (n) {
  let S = n.toString().split("").reverse();
  let i = 0;
  let r = S.map((t) => {
    i++;
    if (i % 3 === 0) {
      if (i != S.length) {
        return "," + t;
      } else {
        return t;
      }
    } else {
      return t;
    }
  })
    .reverse()
    .join("");
  return r;
};

console.log(thousandSeparator(10000000));
console.log(thousandSeparator(1000000000));
