from typing import List

class Solution:
    def maxAscendingSum(self, nums:List[int]) -> int:
        maxSum = nums[0]
        nums.append(0)
        total = 0
        i = 1
        while i < len(nums):
            if nums[i-1] < nums[i]:
                total += nums[i-1]
            else:
                total += nums[i-1]
                if total > maxSum:
                    maxSum = total
                total = 0
            i += 1

        return maxSum

class Solution2:
    def maxAscendingSum(self, nums:List[int]) -> int:
        maxSum = nums[0] 
        nums.append(0)
        total = 0
        for x, y in zip(nums, nums[1:]):
            if x < y:
                total += x
            else:
                total += x
                if total > maxSum:
                    maxSum = total
                total = 0
        return maxSum


answer = Solution2()
print(answer.maxAscendingSum([10,20,30,5,10,50]))
print(answer.maxAscendingSum([10,20,30,40,50]))
print(answer.maxAscendingSum([12,17,15,13,10,11,12]))
print(answer.maxAscendingSum([100,10,1]))

'''
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
Example 4:

Input: nums = [100,10,1]
Output: 100
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
