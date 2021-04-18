from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
    #def maximumWealth(self, accounts) -> int:
        return max([sum(account) for account in accounts])

answer = Solution()
print(answer.maximumWealth([[1,2,3], [3,2,1]]))
print(answer.maximumWealth([[1,5], [7,3], [3,5]]))
