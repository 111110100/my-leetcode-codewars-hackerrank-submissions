from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums = [i for i in nums if i != 0] + [0] * nums.count(0)
        print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.insert(0, nums.count(0))
        for _ in range(nums[0]):
            nums.remove(0)
            nums.append(0)
        nums.remove(nums[0])
        print(nums)

class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.append(nums.pop(i))


class Solution4:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        print(nums)

        
answer = Solution4()
nums = [0,1,0,3,12]
answer.moveZeroes(nums)
