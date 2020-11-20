class Solution:
    def missingNumber(self, nums):
        n = min(nums)
        o = max(nums)
        for _ in nums:
            n += 1
            o -= 1
            if n not in nums:
                return n
            if o not in nums:
                return o

        return


class Solution2:
    def missingNumber(self, nums):
        if len(nums) == 1 and nums[0] == 0:
            return 1
        n = sorted(nums)
        start, end = 0, n[-1]
        return sorted(set(range(start, end + 1)).difference(n))[0]

answer = Solution()
print(answer.missingNumber([0,1]))
print(answer.missingNumber([3,0,1]))
print(answer.missingNumber([9,6,4,2,3,5,7,0,1]))
    

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1)) - set(nums)).pop()

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = [-1] * (len(nums) + 1)
        
        for i in nums:
            res[i] = i
        
        for j in range(len(res)):
            if res[j] == -1:
                return j

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n+1)) // 2) - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=[]
        for k in range(0,len(nums)+1):
            a.append(k)
        return sum(a)-sum(nums)


'''