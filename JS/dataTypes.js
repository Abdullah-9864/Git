// strings

let name = Number("John Doe");
console.log(typeof name);

let num = String(123);
console.log(typeof num);
// numbers

let age = 25;
console.log(age);



if (5 > 0) 
{
  if (10 > 4) 
 {
    console.log("This is true");
 }
 else
 {
    console.log("This is false");
 }
}

let text=(15<18)?"minor":"adult";  //ternary operator 
console.log(text);


let bool=true;
let discount= bool? 0:0;
console.log(discount);


date=new Date().getDay();
console.log(date);
switch(date)
{
   case 0:
      console.log("Monday");
      break;
   case 1:
      console.log("Tuesday");
      break;      
   case 2:
      console.log("Wednesday");
      break;
   case 3:
      console.log("Thursday");
      break;
   case 4:
      console.log("Friday");
      break;
   case 5:
      console.log("Saturday");
      break;
   case 6:
      console.log("Sunday");
      break;
   default:
      console.log("Invalid date");
}

// primitive data types
// 7 types: string, number, boolean, null, undefined, symbol, bigint

// objects and web events 

// non primitive data types

// arrays , objects , functions , dates , regex , maps , sets , weakmaps , weaksets

// //datatypes are based on memory allocation
// Primitive datatypes->  call by value (string,number,boolean,null,undefined,BigInt,symbol) ->Stack memory
// Reference/Non primitive data types -> call by reference ( array,object, function) -> heap memory
// JavaScript is a dynamically typed language. This means that you don't need to specify the data type of a variable when you declare it.


console.log(`My name is ${name} and I am ${age} years old.`);


let gameName= new String("Football");

console.log(gameName);
console.log(gameName.__proto__);


console.log(new Date());
console.log(new Date().getDay());

switch(new Date().getDay())
{
   case 0:
   case 4:
      console.log("Monday");
      break;
   default: 
      console.log("Not Monday");
}



for(var i=0;i<5;i++)
{
   console.log(i);
}

// for loop
result='';
for(var i=0; i<5; i++)
{
   result+=i+" ";
}

console.log(result);

// while loop 
i=5;
_result='';
while(i>0)
{
   _result+=i+" ";
   i--;
}
console.log(_result);


// do while loop
__result='';
i=0;
do 
{
   __result+="hello my name is Abdullah Shahid"+" ";
   i++;
}
while(i<=5);
console.log(__result);


// for of loop

num=  [1,2,3,4,5];
for(let n =0; n<num.length; n++)
{
   console.log(num[n]);
}


let tern=NaN;
let rresult= (tern)? "true":"false";
console.log(rresult);


let x=false;
let y=new Boolean(x);
console.log(x);
console.log(y);   

let name1=null;
let age1=25;
let person=name1??age1;
console.log(person);


