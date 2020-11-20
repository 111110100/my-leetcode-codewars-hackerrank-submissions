class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,e,x = [int(x) for x in str(n)], 1, 0
        for i in s:
            e *= i
            x += i
        return e - x

answer = Solution() # Runtime: 16 ms, faster than 99.90% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
print(answer.subtractProductAndSum(234))
print(answer.subtractProductAndSum(4421))

'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

Constraints:

1 <= n <= 10^5

def subtractProductAndSum(self, n):
    A = map(int, str(n))
    return reduce(operator.mul, A) - sum(A)

def subtractProductAndSum(self, n):
        dm = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        s = repr(n)
        sm, pr = 0, 1
        for c in s:
            pr *= dm[c]
            sm += dm[c]
        return pr-sm

class mySolution:
    def subtractProductAndSum(self, n: int) -> int:
        return eval(str(n).replace('', '*')[1:-1])-eval(str(n).replace('', '+')[1:-1])


'''