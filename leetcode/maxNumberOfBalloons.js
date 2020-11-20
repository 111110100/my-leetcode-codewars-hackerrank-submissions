/**
 * @param {string} text
 * @param {string} subStr
 * @return {number}
 */
var strCount = function (text, subStr) {
  if (text.match(new RegExp(subStr, "g")) != null) {
    return text.match(new RegExp(subStr, "g")).length;
  }
  return 0;
};

/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function (text) {
  let n = strCount(text, "b");
  while (n > 0) {
    if (n == 0) {
      break;
    }
    if (strCount(text, "a") >= n) {
      if (strCount(text, "n") >= n) {
        if (strCount(text, "o") >= n * 2) {
          if (strCount(text, "l") >= n * 2) {
            break;
          } else {
            n -= 1;
          }
        } else {
          n -= 1;
        }
      } else {
        n -= 1;
      }
    } else {
      n -= 1;
    }
  }
  return n;
};

/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons2 = function (text) {
  return Math.min(
    Math.floor(strCount(text, "b")),
    Math.floor(strCount(text, "a")),
    Math.floor(strCount(text, "l") / 2),
    Math.floor(strCount(text, "o") / 2),
    Math.floor(strCount(text, "n"))
  );
};

console.log(maxNumberOfBalloons2("baxxllonob"));
console.log(maxNumberOfBalloons2("loboonbalxbaallpoooonbb"));
console.log(maxNumberOfBalloons2("leetcode"));
console.log(maxNumberOfBalloons2("balon"));
console.log(maxNumberOfBalloons(""));
