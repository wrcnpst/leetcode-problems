function mergeAlternately(word1, word2) {
  let output = "";
  for (let i = 0; i < Math.max(word1.length, word2.length); i++) {
    if (word1[i]) output += word1[i];
    if (word2[i]) output += word2[i];
  }
  return output;
}

mergeAlternately("abc", "pqr");
mergeAlternately("ab", "pqrs");
mergeAlternately("abcd", "pq");
