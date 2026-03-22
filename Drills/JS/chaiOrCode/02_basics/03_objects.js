// singleton objects are objects that can only have one instance. They are often used to represent a single entity or a global state in an application. In JavaScript, you can create a singleton object using an object literal.

// object.create()


// object literals are a way to create objects in JavaScript using a simple syntax. They consist of key-value pairs enclosed in curly braces {}. Each key is a string (or symbol) that represents a property name, and each value can be any valid JavaScript expression.

// const sym =Symbol("sym")
// console.log(typeof sym);

const JSuser=
{
    name:"Abdullah Shahid",
    "institute":"UAF",
    // [sym]: "symbol value",
    age: 21,
    location: "Faisalabad",
    isLoggedIn: true,
    lastLogin: ["Monday", "Tuesday", "Wednesday"], 

}

// console.log(JSuser.name);
// console.log(JSuser["age"]);
// console.log(JSuser.institute);
// console.log(JSuser["institute"]);
// console.log(JSuser[sym]);
// console.log(typeof JSuser[sym]);

// JSuser.name="Ali";
// Object.freeze(JSuser) // This will prevent any modifications to the object
// JSuser.name="Hussain";
// console.log(JSuser.name);
// console.log(JSuser)

JSuser.greeting=function()
{
    console.log("hello world ");
}

JSuser.greetingTwo=function()
{
    console.log(`My name is ${this.name}`);
}
console.log(JSuser.greetingTwo());
console.log(JSuser.greeting());



// let func=function()
// {
//     console.log("hello world");
// }

// func();