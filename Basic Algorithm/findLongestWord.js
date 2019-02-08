function findLongestWordLength(str) {
  let wordArr = str.split(' ');
  let max = 0;
  let longestWord = '';

  wordArr.forEach(word => {
    if(word.length > max) {
      max = word.length;
      longestWord = word;
    }
  });
  console.log("longest word :", longestWord);
  return longestWord.length;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");
findLongestWordLength("May the force be with you");
findLongestWordLength("What if we try a super-long word such as otorhinolaryngology");