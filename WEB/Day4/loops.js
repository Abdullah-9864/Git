let array=[1,2,3,4,5,6,7,8,9,10];
console.log(typeof array);
for(let i=0;i<array.length;i++)
{
    console.log(array[i]);
}

let i=0;
while(i<10)
{
    console.log(i);
    i++;
}



const cars = ["BMW", "Volvo", "Saab", "Ford"];
let len = cars.length;
let text = "";
for (let n=0; n < len; n++) 
{
  text += cars[n] + "<br>";
}
console.log(text);


for(let i=0; i<10; i++)
{
    if(i===3)
    {
        continue;
    }
    console.log(i);
}


// labels are used in nested loops

outer:for(let n=0; n<=3;n++)
{
    for(let m=0;m<=3;m++)
    {
        if(m===2)
        {
            break outer;
        }
        console.log(n,m);
    }
}
