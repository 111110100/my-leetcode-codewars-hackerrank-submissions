/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  return (
    s.replace(/[^a-zA-Z0-9]+/g, "").toLowerCase() ==
    s
      .replace(/[^a-zA-Z0-9]+/g, "")
      .toLowerCase()
      .split("")
      .reverse()
      .join("")
  );
};

console.log(isPalindrome("level"));
console.log(isPalindrome("A man, a plan, a canal: Panama"));
