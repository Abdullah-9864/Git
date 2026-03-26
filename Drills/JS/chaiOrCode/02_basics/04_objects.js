// let appUser= new Object();
// console.log(appUser);

// let appUser={};

// appUser.name="Abdullah Shahid";
// appUser.age=21;



// appUser.regularUser=
// {
//     name:"Ali",
//     age: 22,
// }


// console.log(appUser);

let objOne=
{
    a:1,
    b:2,
}
let objTwo=
{
    c:3,
    d:4,
}
// let mergedObj=Object.assign({}, objOne, objTwo)

let mergedObj={...objOne, ...objTwo}
console.log(mergedObj);
// console.log(mergedObj);
