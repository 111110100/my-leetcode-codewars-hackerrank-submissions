import random
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [n for n in nums if n != 0] + [0] * nums.count(0)
        return nums
        #return [n for n in nums if n != 0] + [0] * nums.count(0)

answer = Solution()
print(answer.moveZeroes([0,1,0,3,12]))
print(answer.moveZeroes([random.randint(0,1) for _ in range(10)]))

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''