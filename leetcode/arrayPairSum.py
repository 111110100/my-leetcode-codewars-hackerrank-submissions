# %%
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        lst = sorted(nums)
        m = 0
        for i in range(0, len(lst), 2):
            m += min([lst[i], lst[i+1]])
        return m 

class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        lst = sorted(nums)
        return sum(lst[0:-1:2])

answer = Solution2()
print(answer.arrayPairSum([1,4,3,2]))
print(answer.arrayPairSum([6,2,6,5,1,2]))
print(answer.arrayPairSum([1, 1, 2, 2, 3, 5, 5, 6, 6, 6]))

