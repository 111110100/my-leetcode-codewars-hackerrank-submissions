String.prototype.toJadenCase = function () {
    s = this.split(' ')
    for (let i = 0; i < s.length; i++) {
        s[i] = s[i][0].toUpperCase() + s[i].slice(1)
    }
    return s.join(' ')
}

t = "How can mirrors be real if our eyes aren't real"

console.log(t.toJadenCase())

/*
String.prototype.toJadenCase = function () { 
    return this.split(" ").map(function(word){
      return word.charAt(0).toUpperCase() + word.slice(1);
    }).join(" ");
  }

String.prototype.toJadenCase = function () {
  return this.replace(/(^|\s)[a-z]/g, function(x){ return x.toUpperCase(); });
};

String.prototype.toJadenCase = function() {
  return this.split(' ').map(item => item[0].toUpperCase() + item.slice(1)).join(' ')
};
*/