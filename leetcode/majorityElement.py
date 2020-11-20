import random
class Solution:
    def majorityElement(self, nums):
        p = set(nums)
        d = {}
        for q in p:
            d[q] = nums.count(q)
        d = {k: v for k, v in sorted(d.items(), key=lambda i: i[1], reverse=True)}
        f, *r = d
        return f 

answer = Solution()
print(answer.majorityElement([3,2,3]))
print(answer.majorityElement([2,2,1,1,1,2,2]))
print(answer.majorityElement([4,2,1,1,1,1,2,2]))

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

class Solution:
    def majorityElement(self, nums):
        element, cnt = 0, 0
        for e in nums:
            if element == e:
                cnt += 1
            elif cnt == 0:
                element, cnt = e, 1
            else:
                cnt -= 1

        return element

class Solution:
    def majorityElement(self, nums):
        num_count = defaultdict(int)
        majority = len(nums) // 2
        
        for num in nums:   
            num_count[num] += 1
            if num_count[num] > majority:
                return num
'''