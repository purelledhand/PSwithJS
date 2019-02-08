function largestOfFour(arr) {
  const reducer = (x,y) => Math.max(x,y);

  let largeArr = [];
  arr.map(group => {
    largeArr.push(group.reduce(reducer));
  });

  console.log(largeArr);
  return largeArr;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]);