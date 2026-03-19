let expression="";

function pressKey(value)
{
    if (value === "=") 
        {
    try {
        expression = String(eval(expression));
        document.getElementById("display").innerText = expression;
    } 
    catch {
        document.getElementById("display").innerText = "Syntax Error";
        expression = "";
    }
   } 
    else if(value==="back")
    {
        expression = expression.slice(0, -1);
        document.getElementById("display").innerText=expression;

    }
    else if(value==="C")
    {
        expression = "";
        document.getElementById("display").innerText=expression;
    }
    else
    {
        expression += value;
        document.getElementById("display").innerText=expression;
    }
}

document.addEventListener("keydown", function(event) {
    if ("0123456789".includes(event.key)) {
        pressKey(event.key);
    } else if ("+-*/".includes(event.key)) {
        pressKey(event.key);
    } else if (event.key === "Enter") {
        pressKey("=");
    } else if (event.key === "Backspace") {
        pressKey("back");
    } else if (event.key === "Delete"){
        pressKey("C");
    }
});


