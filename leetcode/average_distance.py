class Solution:
    def average_distance(self, a, b):
        dist = []
        for x, y in zip(a, b):
            dist.append((x - y)**2)
        return sum(dist)/len(a)
            


answer = Solution()
print(answer.average_distance([1,2,3],[4,5,6]))