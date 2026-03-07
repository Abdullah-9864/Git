// primitive data types in JavaScript include:
// 1. Number: represents both integer and floating-point numbers. Example: 42, 3.14
// 2. String: represents a sequence of characters. Example: "Hello, World!"
// 3. Boolean: represents a logical entity that can be either true or false. Example: true, false
// 4. Null: represents the intentional absence of any object value. Example: null
// 5. Undefined: represents a variable that has been declared but has not been assigned a value. Example: undefined
// 6. Symbol: represents a unique identifier. Example: Symbol('description')
// 7. BigInt: represents integers with arbitrary precision. Example: 123n, BigInt("12345678901234567890")


// Non primitive or Reference data types in JavaScript include:
// 1. Object: represents a collection of properties and methods. Example: { name: "Alice", age: 30 }
// 2. Array: represents an ordered list of values. Example: [1, 2, 3, "four"]
// 3. Function: represents a reusable block of code that performs a specific task. Example: function greet() { console.log("Hello!"); }
// 4. Date: represents a specific point in time. Example: new Date()
// 5. RegExp: represents a regular expression, which is used for pattern matching in strings. Example: /abc/   
// 6. Map: represents a collection of key-value pairs. Example: new Map()
// 7. Set: represents a collection of unique values. Example: new Set([1, 2, 3])
const ID=Symbol("id")

const anotherID=Symbol("id")

console.log(ID===anotherID)

const myFunction=function()
{
    console.log("this is print function")
}

console.log(typeof myFunction)

