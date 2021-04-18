from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for num in nums if len(str(num)) % 2 == 0])

class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for i in nums if 9 < i < 100 or 999 < i < 10000 or 99999 < i < 1000000)

answer = Solution2()
input = [5555,901,482,1771,11]
print(answer.findNumbers(input))
