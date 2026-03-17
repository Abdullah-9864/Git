var accountId=14453;
const accountEmail='abdullahshahid093@hotmail.com'
const accountPassword ="1234"
const accountCity="jaipur"

accountId=2134;

console.table([accountId,accountEmail,accountPassword ,accountCity])


//Block scope and declaration type explained
if (true) {
  let blockVar = "I'm inside the block!";
  const blockConst = "Me too!";
  var functionVar = "I'm not block-scoped!";
  console.log(blockVar); // Works: "I'm inside the block!"
  console.log(blockConst); // Works: "Me too!"
  console.log(functionVar);
}

//console.log(blockVar); // ERROR: blockVar is not defined
//console.log(blockConst); // ERROR: blockConst is not defined
console.log(functionVar); // Works: "I'm not block-scoped!" (var is function-scoped)
