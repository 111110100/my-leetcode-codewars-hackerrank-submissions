from typing import List

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return nums[middle]
        return False

answer = Solution()
print(answer.binarySearch([1,3,5,6], 5))
print(answer.binarySearch([1,3,5,6], 2))
print(answer.binarySearch([1,3,5,6], 6))
print(answer.binarySearch([1,3,5,6], 0))
