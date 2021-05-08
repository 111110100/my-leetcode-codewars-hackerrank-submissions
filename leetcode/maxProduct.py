from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = sorted(nums)
        return (l[-1]-1) * (l[-2]-1)

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        m, n = nums.pop(nums.index(max(nums)))-1, max(nums)-1
        return m * n

answer = Solution2()
print(answer.maxProduct([3,4,5,2]))
