class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) < len(nums)

class Solution2:
    def containsDuplicate(self, nums) -> bool:
        n = sorted(nums)
        for x, y in zip(n, n[1:len(n)]):
            print(x, y)
            if x == y:
                return True
        return False


answer = Solution2()
print(answer.containsDuplicate([3,1]))
#print(answer.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
#print(answer.containsDuplicate([1,4,3,2]))

'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''