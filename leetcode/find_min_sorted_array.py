from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(array, low, high):
            if high < low:
                return array[0]

            if high == low:
                return array[low]

            middle = int((low + high)/2)

            if middle < high and array[middle + 1] < array[middle]:
                return array[middle + 1]

            if middle > low and array[middle] < array[middle - 1]:
                return array[middle]

            if array[high] > array[middle]:
                return find_min(array, low, middle - 1)

            return find_min(array, middle + 1, high)

        n = len(nums)
        return find_min(nums, 0, n - 1)

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
