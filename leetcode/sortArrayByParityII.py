class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        even, odd = (a for a in A if not a % 2), (a for a in A if a % 2)
        return [y for x in zip(even,odd) for y in x]

class Solution2:
    def sortArrayByParityII(self, A: list) -> list:
        odd = [x for x in A if not x % 2]
        even =  [x for x in A if x % 2]

        result = []

        for x, y in zip(even, odd):
            result.append(x)
            result.append(y)        # join even and odd numbers starting from even

        return result

answer = Solution2()
print(answer.sortArrayByParityII([4,2,5,7]))

'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''
