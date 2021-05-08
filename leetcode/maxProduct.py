from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = sorted(nums)
        return (l[-1]-1) * (l[-2]-1)

answer = Solution()
print(answer.maxProduct([3,4,5,2]))
