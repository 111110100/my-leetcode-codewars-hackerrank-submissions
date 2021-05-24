from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1 
        t = [p:=p*v for v in nums]
        return 1 if p > 0 else -1 if p < 0 else 0 

answer = Solution()
print(answer.arraySign([-1,-2,-3,-4,3,2,1]))
print(answer.arraySign([1,5,0,2,-3]))
print(answer.arraySign([-1,1,-1,1,-1]))

'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100

class Solution:
    def arraySign(self, nums: List[int]) -> int:  # 68 ms
        import functools
        product = functools.reduce(int.__mul__, nums)
        return (product > 0) - (product < 0)

    def arraySign(self, nums: List[int]) -> int:  # 64 ms
        import functools
        return (product > 0) - (product < 0) if any((product := functools.reduce(int.__mul__, nums),)) else product

    def arraySign(self, nums: List[int]) -> int:  # 108 ms
        import itertools
        *_, product = itertools.accumulate(nums, int.__mul__)
        return (product > 0) - (product < 0)

    def arraySign(self, nums: List[int]) -> int:  # 112 ms
        return 0 if 0 in nums else -1 if sum(1 for i in nums if i < 0) % 2 else 1

    def arraySign(self, nums: List[int]) -> int:  # 60 ms
        return 0 if 0 in nums else -1 if str(nums).count("-") % 2 else 1

    def arraySign(self, nums: List[int]) -> int:  # 88 ms
        n_negatives = 0
        for n in nums:
            if n == 0:
                return 0
            n_negatives += n < 0
        return -1 if n_negatives % 2 else 1

    def arraySign(self, nums: List[int]) -> int:  # 124 ms
        positive = 1
        for n in nums:
            if n == 0:
                return 0
            positive ^= n < 0
        return (-1, 1)[positive]
'''
