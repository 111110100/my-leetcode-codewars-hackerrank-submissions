from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

class Solution2:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) == 1 and target[0] == arr[0]:
            return True
        target.sort()
        arr.sort()
        for x,y in zip(target,arr):
            if x!=y:
                return False
        return True

answer = Solution2()
target = [360, 392]
arr = [392, 360]
print(answer.canBeEqual(target, arr))
