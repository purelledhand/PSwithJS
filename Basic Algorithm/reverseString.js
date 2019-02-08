function reverseString(str) {
  let reverseStr="";
  for(let i=str.length-1; i>=0;i--) {
    reverseStr += str[i];
  }
  return reverseStr;
}

console.log(reverseString("hello"));

/**
 * ㅇㅏ무생각 없이 reverseStr.concat(str[i]) 했는데 안됐다.
 * String.concat 메서드는 concat 한 값을 리턴할 뿐 String 자체 value에 영향을 주지 않는다.
 */