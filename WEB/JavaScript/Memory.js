const { memo } = require("react");

let myAccountBalance=1000;
let myOtherAccountBalance=myAccountBalance;
myOtherAccountBalance=5000;
console.log(myAccountBalance);
console.log(myOtherAccountBalance);

// so in primitive data types, when we assign a variable to another variable, it creates a copy of the value. So when we change the value of one variable, it does not affect the other variable. This is because they are stored in different memory locations.
// this is called pass by value. it uses stack memory to store the values of primitive data types.


let user=
{
    name:"ali",
    age:20,
    city:"Islamabad"
}

// user object is stored in heap memory and when we assign it to another variable, it does not create a copy of the object, but rather it creates a reference to the same object in memory. So when we change the value of one variable, it affects the other variable as well because they are both referencing the same object in memory. This is called pass by reference.

let user1=user;

// user1 is using reference to the same object in memory as user, so when we change the value of user1, it also changes the value of user because they are both referencing the same object in memory.
user1.name="ahmed";
console.log(user);
console.log(user1);
