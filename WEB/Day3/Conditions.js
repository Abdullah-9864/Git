// var hour=8;
// if(hour<18)
// {
//     greeting = "good day";
// }
// console.log(greeting);

// let age=89;
// let text="you cannot drive.";

// if(age>=18)
// {
//     text="you can drive.";
// }

// console.log(text)


// let text0;
// if (Math.random() < 0.5) 
// {
//   text0 = "<a href='https://w3schools.com'>Visit W3Schools</a>";
// }
// else 
// {
//   text0 = "<a href='https://wwf.org'>Visit WWF</a>";
// }
// document.getElementById("demo").innerHTML = text0;



let day;

switch(new Date().getDay())
{
  case 0:
    day="Sunday";
    break;
  case 1:
    day="Monday"; 
    break;  
  case 2:
    day="Tuesday";
    break;
  case 3:
    day="Wednesday";
    break;
  case 4:
    day="Thursday"; 
    break;
  case 5:
    day="Friday";
    break;
  case 6:
    day="Saturday";
    break;
  default:
    day="Unknown day";

}
document.getElementById("day").innerHTML=day;


function checkAge()
{
  let variable;
  variable=document.getElementById("input").value;
  let condition=(variable<=13)?"Too young":(variable<=18)?"Young":"Adult";
  console.log(condition);
  document.getElementById("result").textContent=condition;
}




let x = 6;
let y = 3;
let z = (x < 10 && y > 1)
console.log(z);


let age=null;
console.log(age??0);



// nullish coalesing operator (??) returns the right-hand operand when the left-hand operand is null or undefined, otherwise it returns the left-hand operand. In this example, since age is null, the expression age ?? 0 will evaluate to 0.













