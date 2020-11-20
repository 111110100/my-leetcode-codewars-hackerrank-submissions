class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max(''.join([str(i) for i in nums]).split('0')))

'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

    count = maxCount = 0
        
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            maxCount = max(count, maxCount)
            count = 0
            
    return max(count, maxCount)

    count = 0
    res = []
    
    if len(nums) == 0:
        return 0
    else:
        for i in nums:
            if i == 1:
                count += 1
                
            else:
                res.append(count)
                count = 0
        res.append(count)
    return max(res)
'''