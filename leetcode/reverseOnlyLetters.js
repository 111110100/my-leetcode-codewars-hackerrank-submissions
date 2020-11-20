/**
 * @param {string} S
 * @return {boolean}
 */
var isLetter = function (S) {
  return S.length === 1 && S.toLowerCase() != S.toUpperCase();
};

/**
 * @param {string} S
 * @return {string}
 */
var reverseOnlyLetters = function (S) {
  let letters = S.split("").filter((char) => isLetter(char));
  let out = "";
  for (let i = 0; i < S.length; i++) {
    if (isLetter(S[i])) {
      out += letters.pop();
    } else {
      out += S[i];
    }
  }
  return out;
};

/**
 * @param {string} S
 * @return {string}
 */
var reverseOnlyLetters2 = function (s) {
  const A = s.match(/[a-z]/gi);
  return s.replace(/[a-z]/gi, () => A.pop());
};

console.log(reverseOnlyLetters("ab-cd"));
