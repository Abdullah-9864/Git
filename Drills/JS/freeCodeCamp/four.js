for(let a=1;a<=5;a++)
{
    for(let b=1; b<=5-a;b++)
        process.stdout.write(" ");
    for(let c=1; c<=a; c++)
        process.stdout.write("*");
    process.stdout.write("\n");
}



let str="12"
console.log(typeof str)