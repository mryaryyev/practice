console.log("MITASK")

// E-TASK
/*
Shunday function tuzing,
u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh".
*/
function getReverse(a) {
    let b = a.split(""); //convert string to array
    return b.reverse().join(""); //reverse in array and convert it to string
}

const getReverse1 = getReverse("hello");
console.log(getReverse1);

const getReverse2 = getReverse("goodbye")
console.log(getReverse2);