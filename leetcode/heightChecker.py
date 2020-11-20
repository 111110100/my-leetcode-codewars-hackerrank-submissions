class Solution:
    def heightChecker(self, heights):
        return [x == y for x, y in zip(heights, sorted(heights))].count(False)


answer = Solution()
print(answer.heightChecker([1,2,4,2,5]))
print(answer.heightChecker([10,6,6,10,10,9,8,8,3,3,8,2,1,5,1,9,5,2,7,4,7,7]))