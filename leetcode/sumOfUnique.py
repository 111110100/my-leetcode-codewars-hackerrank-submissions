from typing import List
import collections

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq = []
        [uniq.append(num) for num in nums if nums.count(num) == 1]
        return sum(uniq)

class Solution2:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in collections.Counter(nums).items() if v == 1)

class Solution3:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num in nums if nums.count(num) == 1)

answer = Solution()
input = [1,2,3,4,5,5,4]
print(answer.sumOfUnique(input))
