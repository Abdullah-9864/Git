



// data types

// primitive data types




// string, number, boolean, null, undefined, symbol, bigint

// arrays, objects, functions, etc. are non-primitive data types.


let c=12;
let d=c;

c=c+2;
console.log(c); //14
console.log(d); //12

let a=[1,2,3];
let b=a;
a.push(4);
console.log(a); //[1,2,3,4]
console.log(b); //[1,2,3,4] because a and b are referencing the same array in memory. They are not copies of each other. They are both pointing to the same array in memory. So when we modify the array through a, it also modifies the array that b is pointing to.
a.push(5);
console.log(a); //[1,2,3,4,5]
console.log(b); //[1,2,3,4,5] because a and b are referencing the same array in memory. They are not copies of each other. They are both pointing to the same array in memory. So when we modify the array through a, it also modifies the array that b is pointing to.