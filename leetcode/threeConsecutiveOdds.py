class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        c = 0
        for v in arr: 
            c += 1 if v % 2 != 0 else -c
            if c > 2:
                return True
        return False

answer = Solution()
print(answer.threeConsecutiveOdds([2,6,4,1]))
print(answer.threeConsecutiveOdds([4,2,34,3,4,5,7,23,12]))

'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return "111" in "".join([str(x%2) for x in arr])
'''