from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        t = 0
        for word in words:
            for c in allowed:
                word = word.replace(c, "")
            t += 1 if len(word) == 0 else 0
        return t

class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len([word for word in words if all([char in allowed for char in set(word)])])

class Solution3:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        t = 0
        for word in words:
            d = set(word)
            t += 1 if all([c in allowed for c in d]) else 0
        return t


answer = Solution2()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(answer.countConsistentStrings(allowed, words))
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(answer.countConsistentStrings(allowed, words))
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(answer.countConsistentStrings(allowed, words))