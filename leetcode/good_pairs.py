def numIdenticalPairs(nums):
    gp = 0
    for x, i in enumerate(nums):
        for y, j in enumerate(nums):
            if x != y:
                if i == j and x < y:
                    gp += 1
    return gp


print(numIdenticalPairs([1,2,3,1,1,3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))

'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
def numIdenticalPairs(self, nums: List[int]) -> int:
    return sum(v * (v - 1) // 2 for v in Counter(nums).values())

def numIdenticalPairs(self, nums: List[int]) -> int:
    i = 0
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            if x<y and nums[x] == nums[y]:
                i += 1
    return i
'''