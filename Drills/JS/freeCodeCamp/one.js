console.log("hello asad");
var a=10; //hello world is over now its about declaring variables


/*data types in js
String
Number
Boolean
Null
Undefined
Symbol
Object*/


var myname="asad";
myname="abd";
console.log(myname);

// other ways to declare variables
let myname2="asad";
// AND 
var myname3="asad";
//let and const are block scoped and var is function scoped
//let and const are introduced in ES6 and var is the old way of declaring variables
//const is used to declare constants and its value cannot be changed
// let is used to declare variables that can be reassigned means that we can change the value of a variable declared with let but we cannot change the value of a variable declared with const
//var is function scoped and can be redeclared and reassigned

let ourplanet="earth";
const pi=3.14;
// pi=3.14159; // this will give an error because pi is a constant and its value cannot be changed
console.log(ourplanet);
console.log(pi);
ourplanet="mars"; // this will work because ourplanet is a variable that can be reassigned
console.log(ourplanet);

// storing values with assignment operator
let b;
console.log(b);
