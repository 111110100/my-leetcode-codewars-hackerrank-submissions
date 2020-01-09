class Solution:
    def sortArrayByParity(self, A: list) -> list:
        return [a for a in A if not a % 2] + [a for a in A if a % 2]

class Solution2(object):
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for number in A:
            if number % 2 == 0:         # if remainder is equal 0, the number is even
                even.append(number)     # add to even
            else:
                odd.append(number)      # when remainder isn't equal 0, it's odd so add to odd

        return even + odd               # + sign joins to lists

class Solution3:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [even for even in A if even % 2 == 0] + [odd for odd in A if odd % 2 ==1]

answer = Solution3()
print(answer.sortArrayByParity([3,1,2,4]))

'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
'''
