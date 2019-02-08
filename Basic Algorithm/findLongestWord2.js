function findLongestWordLength(str) {
  const reducer = (acc, str) => Math.max(acc,str.length);

  return str.split(' ')
    .reduce(reducer, 0);
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));