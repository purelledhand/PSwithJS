function reverseString(str) {
  let reverseStr="";
  for(let i=str.length-1; i>=0;i--) {
    reverseStr += str[i];
  }
  return reverseStr;
}

function reverseString2(str) {
  return str.split('').reverse().join('');
}

console.log(reverseString("hello"));
console.log(reverseString2("hello"));

