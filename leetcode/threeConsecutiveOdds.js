/**
 * @param {number[]} arr
 * @return {boolean}
 */
function threeConsecutiveOdds(arr) {
  let c = 0;
  for (let i = 0; i < arr.length; i++) {
    c += arr[i] % 2 != 0 ? 1 : -c;
    if (c > 2) {
      return true;
    }
  }
  return false;
}

var threeConsecutiveOdds2 = function (arr) {
  for (let i = 0; i < arr.length - 2; i++) {
    if (arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0) {
      return true;
    }
  }
  return false;
};

console.log(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]));
console.log(threeConsecutiveOdds([1])); // does not give index out of range error
