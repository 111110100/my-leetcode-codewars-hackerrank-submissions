class Solution:
    def average(self, salary) -> float:
        return (sum(salary)-(min(salary)+max(salary))) / (len(salary) - 2)


answer = Solution()
print(answer.average([4000,3000,1000,2000]))
print(answer.average([8000,9000,2000,3000,6000,1000]))