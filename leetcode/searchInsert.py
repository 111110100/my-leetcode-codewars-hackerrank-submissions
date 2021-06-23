class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)
        bottom = 0
        top = len(nums) - 1
        while bottom <= top:
            middle = top - bottom // 2
            if nums[middle] > target:
                top = middle - 1
            elif nums[middle] < target:
                top = middle + 1
            else:
                return middle

class Solution2: # ^ is not O(log n)
    def searchInsert(self, nums, target):
        bottom = 0
        top = len(nums)
        while bottom < top:
            middle = (bottom + top) // 2
            if nums[middle] > target:
                top = middle - 1
            elif nums[middle] < target:
                bottom = middle + 1
            else:
                return middle

        return top if bottom == len(nums) else bottom if nums[bottom] >= target else bottom + 1

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""
