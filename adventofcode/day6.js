let answers = `abc

a
b
c

ab
ac

a
a
a
a

b
`.split("\n");

let line = "";
let total = [];
for (let i = 0; i < answers.length; i++) {
  if (answers[i] == "") {
    total.push(new Set(line).size);
    line = "";
  } else {
    line += answers[i];
  }
}

console.log(total.reduce((n1, n2) => n1 + n2));
