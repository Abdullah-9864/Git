
// Arithematic operators
let x=10;
let y=40;
x++;
z=x+y;
z--;
console.log(z);

// Assignment Operators
text0="hey there";
text0+=" how are you!";
console.log(text0)

// Comparison Operator

text1="hwlo";
console.log(text0==text1);


// Logical Operator

statement0=true;
statement1=false;

console.log(statement0||statement1)


// ______________________________________________________________________
function checkAge()
{
let age=document.getElementById("input").value;
age=Number(age);

let voteable;
if(isNaN(age))
{
    voteable="input is not a number";

}
else
{
    voteable=(age<18)?
    "too young":"old enough";
}
document.getElementById("result").textContent=voteable;
}




