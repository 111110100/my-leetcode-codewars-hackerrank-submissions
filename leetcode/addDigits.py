class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            d = [int(x) for x in list(str(num))]
            if len(d) == 1:
                break
            num = sum(d)
        return d[0] 

class Solution2:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1

answer = Solution2()
print(answer.addDigits(38))
print(answer.addDigits(555))

'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''