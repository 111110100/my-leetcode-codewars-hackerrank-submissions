/**
 * @param {number[]} A
 * @return {boolean}
 */
var isMonotonic = function (A) {
  let a = [];
  let b = [];
  for (let i = 0; i < A.length - 1; i++) {
    a.push(A[i] <= A[i + 1]);
    b.push(A[i] >= A[i + 1]);
  }
  return !a.includes(false) || !b.includes(false);
};

console.log(isMonotonic([1, 2, 2, 3]));
console.log(isMonotonic([6, 5, 4, 4]));
console.log(isMonotonic([1, 3, 2]));
