function countSheeps(arrayOfSheep) {
    return arrayOfSheep.filter(x => x).length
}

function countSheeps2(arrayOfSheep) {
    let sheeps = 0
    for (let i = 0; i < arrayOfSheep.length; i++) {
        if (arrayOfSheep[i] === true) {
            sheeps++
        }
    }
    return sheeps
}

let sheeps = [true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true ];

console.log(countSheeps(sheeps))

/*
function countSheeps(arrayOfSheeps) {
  return arrayOfSheeps.filter(Boolean).length;
}


*/