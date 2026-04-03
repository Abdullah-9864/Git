// varible=34;
// console.log(varible);
// console.log(typeof variable)

// var newVar=232;
// var newVar=454;
// console.log(newVar);

// const tinderUser={};
// tinderUser.id="123abc";
// tinderUser.name="abdullah";
// console.log(tinderUser);


// const regularUser={
//     email: "abd@gmail.com",
//     fullName:{
//         userFullName:{
//             firstName:"abdullah",
//             lastName:"shahid"
//         }
//     }
// };

// console.log(regularUser);

// const obj1={1:"a", 2:"b"}
// const obj2={3:"a", 4:"b"}

// const obj3=Object.assign(obj1,obj2)
// console.log(obj3);
// const obj4={...obj1, ...obj2};
// console.log(obj4);


// let array=
// [
//     1,2,3,4,

//     {
//         Name:"abdullah",
//         Age:21
//     },
//     {
//         Name:"Asad",
//         Age:18
//     }
// ];
// console.log(array);



let string = "Abdullah Shahid";
let text="  Hello world  ";

console.log("hello,"+ string);

console.log(`hello world my name is ${string}`);
console.log(string.length);

console.log(string.toUpperCase());
console.log(string.toLowerCase());

console.log(string.charAt(3));
console.log(string.substring(0,5));

console.log(string.split(""));

console.log(string.replace("Shahid","hello"));

console.log(string.includes("Shahid"));

console.log(text.trim());

console.log(3>4);

console.log("Hello world this is \"Abdullah\"")

console.log(text.split("").reverse().join(""));



function isPalindrome(str)
{
    let reversedStr=str.split("").reverse().join("");
    return str===reversedStr;
};

console.log(isPalindrome("olo"));



