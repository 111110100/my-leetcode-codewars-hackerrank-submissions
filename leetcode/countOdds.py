#%%
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return sum([1 for i in range(low, high+1) if i % 2 != 0]) 

 # for big numbers
class Solution2:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            return (high - low + 1) // 2
        else:
            return (high - low + 2) // 2

answer = Solution2()
print(answer.countOdds(800445804,979430543))
# %%
