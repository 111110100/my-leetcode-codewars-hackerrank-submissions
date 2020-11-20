/**
 * @param {number[]} ar
 * @return {number}
 */
var birthdayCakeCandles = function (ar) {
  let mar = Math.max(...ar);
  return ar.map((candle) => mar == candle).reduce((a, b) => a + b, 0);
};

let candles = [4, 1, 2, 4, 4];
console.log(birthdayCakeCandles(candles));
