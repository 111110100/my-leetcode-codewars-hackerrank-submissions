from typing import List
import collections

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq = []
        [uniq.append(num) for num in nums if nums.count(num) == 1]
        return sum(uniq)

class Solution2:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in collections.Counter(nums).items() if v == 1)

class Solution3:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(num for num in nums if nums.count(num) == 1)

answer = Solution()
input = [1,2,3,4,5,5,4]
print(answer.sumOfUnique(input))

'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
