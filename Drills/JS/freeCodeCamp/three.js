array=[[1, 2, 3], [4, 5, 6], [[7, 8, 9],9,8]];
console.log(array[2][0][1]); // this will give us 8 because array[2] will give us [[7, 8, 9],9,8] and then array[2][0] will give us [7, 8, 9] and then array[2][0][1] will give us 8
newArray=["hello", "world", "cat"];
newArray.push(["dog","ali"]); // this will add "dog" to the end of the array
console.log(newArray);

newArray.pop(newArray.len-1); // this will remove the last element of the array which is ["dog","ali"]
console.log(newArray);



