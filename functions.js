function sayMyName(num1,num2)
{
    //  console.log(num1+num2);
     return num1+num2;
}
sayMyName(1,4);
// console.log(result);



function loginUserMessage(username)
{
    return `${username} just logged in`;

}

console.log(loginUserMessage("Abdullah"));




let nrToStr=6;
nrToStr=String(nrToStr);
console.log(nrToStr, typeof(nrToStr));



let strToNr="hello"    ;
strToNr=Number(strToNr);
console.log(strToNr, typeof(strToNr));


let strToBool = 0;
strToBool = Boolean(strToBool);
console.log(strToBool, typeof strToBool);

