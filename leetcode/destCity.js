/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
  let cities = []
  for (let i = 0; i < paths.length; i++) {
    cities.push(paths[i][0])
  }
  for (let i = 0; i < paths.length; i++) {
    if (!cities.includes(paths[i][1])) {
      return paths[i][1]
    }
  }
};



console.log(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
console.log(destCity([["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))
console.log(destCity([["B","C"],["D","B"],["C","A"]]))
console.log(destCity([["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]))
