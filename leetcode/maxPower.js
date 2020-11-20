/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function(s) {
  let n = 1
  let p = 1
  for (let i = 0; i < s.length; i++) {
    if (s[i] == s[i+1]) {
      n += 1
      if (p < n) {
        p = n
      }
    } else {
      n = 1
    }
  }
  return p
};

console.log(maxPower('leetcode'))
console.log(maxPower('abbcccddddeeeeedcba'))
console.log(maxPower('triplepillooooow'))