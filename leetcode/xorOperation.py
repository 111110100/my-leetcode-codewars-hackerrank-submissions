class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums, x = [], start
        [nums.append(start + (2 * i)) for i in range(n)]
        for n in nums[1:]:
            x ^= n
        return x

class Solution2:
    def xorOperation(self, n: int, start: int) -> int:
        x = start
        for i in range(n):
            if (start + 2 * i) != start:
                x ^= start + (2 * i)
        return x

class Solution3:
    def xorOperation(self, n: int, start: int) -> int:
        x = 0
        for i in range(n):
            x ^= start + 2 * i
        return x


answer = Solution2()
print(answer.xorOperation(5,0))
print(answer.xorOperation(4,3))
print(answer.xorOperation(1,7))
print(answer.xorOperation(10,5))
