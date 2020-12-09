const longWord = (word, count) => {
  const wordList = word.split('');
  if (wordList.length > count) {
    return [wordList[0], wordList.length - 2, wordList[wordList.length - 1]].join('');
  }
  return word;
};

console.log(longWord('pneumonoultramicroscopicsilicovolcanoconiosis', 4));
