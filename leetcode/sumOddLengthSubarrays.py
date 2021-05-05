from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        size = len(arr)
        chunk = len(arr)
        total = 0
        while chunk >= 1:
            index = 0
            while index + chunk <= size:
                total += sum(arr[index:index+chunk:])
                index += 1
            chunk -= 2
        return total
        
class Solution2:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for length in range(1, len(arr)+1, 2):
            i = 0
            while i+length <= len(arr):
                s += sum(arr[i:i+length])
                i += 1
        return s

answer = Solution()
input = [1,4,2,5,3]
print(answer.sumOddLengthSubarrays(input))
input = [1,2]
print(answer.sumOddLengthSubarrays(input))
input = [10,11,12]
print(answer.sumOddLengthSubarrays(input))

'''
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
'''