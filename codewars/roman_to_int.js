function solution(roman){
  // complete the solution by transforming the 
  // string roman numeral into an integer  
  let dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  let s
  s = roman.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')
  let n = 0
  for (let c of s) {
    n += dict[c]
  }

  return n
}

console.log(solution('MDCLXVI'))
