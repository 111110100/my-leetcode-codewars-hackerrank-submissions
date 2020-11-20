class Solution:
    def stringMatching(self, words):
        r = []
        for x in range(len(words)):
            for y in range(len(words)):
                if words[x] != words[y] and words[x] in words[y] and words[x] not in r:
                    r.append(words[x])
        return r

class Solution2():
    def stringMatching(self, words):
        return list({key for key in words for word in words if key != word and key in word})

class Solution3():
    def stringMatching(self, words):
        a = ' '.join(words)
        return [e for e in words if a.count(e) >= 2]

answer = Solution2()
print(answer.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))

'''
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []


'''