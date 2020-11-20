class Solution:
    def isMonotonic(self, A):
        r = [x <= y for x, y in zip(A, A[1:])]
        p = [x >= y for x, y in zip(A, A[1:])]
        return not False in r or not False in p


answer = Solution()
print(answer.isMonotonic([6, 5, 4, 4, 5]))
print(answer.isMonotonic([1, 2, 2, 3]))

'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

    def isMonotonic(self, A):
        return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return True if len(A) == 1 else all(A[i] - A[i-1] >= 0 for i in range(1,len(A))) or all(A[i] - A[i-1] <= 0 for i in range(1,len(A)))
'''