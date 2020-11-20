class Solution:
    def singleNumber(self, nums):
        return nums[[nums.count(x) == 1 for x in nums].index(True)]

class Solution2:
    def singleNumber(self, nums):
        n = 0
        for i in nums:
            n ^= i 
        return n

answer = Solution2()
print(answer.singleNumber([4,1,2,1,2]))
print(answer.singleNumber([2,2,1]))
print(answer.singleNumber([2,1,1,2,4,5,3,6,4,5,6]))

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''