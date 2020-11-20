/**
 * @param {string} arr
 * @param {string} val 
 * @return {number}
 */
const countChar = (arr, val) => arr.split("").reduce((a, v) => (v === val ? a + 1 : a), 0)

/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    return countChar(moves, "U") === countChar(moves, "D") && countChar(moves, "L") === countChar(moves, "R")
};

/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle2 = function(moves) {
  let [U, D, L, R] = [0, 0, 0, 0]
  for (let i = 0; i < moves.length; i++) {
    switch(moves[i]) {
      case "U":
        U++
        break
      case "D":
        D++
        break
      case "L":
        L++
        break
      case "R":
        R++
        break
    }
  }
  return U === D && L === R
}

console.log(judgeCircle2("UD"))
console.log(judgeCircle2("LLLL"))