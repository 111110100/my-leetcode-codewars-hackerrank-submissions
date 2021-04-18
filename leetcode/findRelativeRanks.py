#%%
from typing import List

class Solution:
    def getRank(self, rank: int) -> str:
        return {
            1: 'Gold Medal',
            2: 'Silver Medal',
            3: 'Bronze Medal'
        }.get(rank, str(rank))

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {}
        for a in score[::-1]:
            rank.setdefault(a, self.getRank(len(rank) + 1))
        return [rank[i] for i in score]


class Solution2:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {n: i for i, n in enumerate(sorted(score, reverse=True))}
        medals = ['Gold', 'Silver', 'Bronze']
        return [str(rank[n]+1) if rank[n] >= len(medals) else (medals[rank[n]] + ' Medal') for n in score]

answer = Solution2()
print(answer.findRelativeRanks([10,3,8,9,4]))
# %%
