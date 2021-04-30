/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
  let maxCandies = Math.max(...candies)
  return candies.map((candy) => candy + extraCandies >= maxCandies)
};

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
const kidsWithCandies2 = (candies, extraCandies) => {
  const ret = []
  let max = 0
  for (const val of candies) {
    val > max && (max = val)
  }
  for (let i = 0; i < candies.length; ++i) {
    ret.push(candies[i] + extraCandies >= max)
  }
  return ret
};

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
const kidsWithCandies3 = function(candies, extraCendies) {
  const max = Math.max.apply(Number, candies)
  return candies.map((candy) => {
    return candy + extraCandies >= max ? true : false;
  })
}

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
const kidsWithCandies4 = function(candies, extraCendies) {
  const max = Math.max.apply(Number, candies)
  let ret = candies.map((candy) => {
    return candy + extraCandies >= max ? true : false;
  }) 
  return ret
}

var candies = [4,2,1,1,2]
var extraCandies = 1
//console.log(kidsWithCandies(candies, extraCandies))
console.log(kidsWithCandies4(candies, extraCandies))
