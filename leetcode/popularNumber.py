class Solution:
    def popularNumber(self, nums):
        return max(set(nums), key = nums.count)

answer = Solution()
print(answer.popularNumber([1,2,3,2,2,3,1,1,1]))