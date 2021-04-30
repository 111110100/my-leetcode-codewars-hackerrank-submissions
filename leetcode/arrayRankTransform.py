class Solution:
    def arrayRankTransform(self, arr):
        if len(arr) == 0:
            return []
        r, m, p = 1, {}, min(arr) - 1
        for x in sorted(arr):
            if x > p:
                m[x] = r
                r += 1
                p = x

        return [m[i] for i in arr]


answer = Solution()
print(answer.arrayRankTransform([40, 10, 20, 30]))
# print(answer.arrayRankTransform([10,10,10,20]))

'''
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 
Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 
Constraints:

0 <= arr.length <= 10^5
-10^9 <= arr[i] <= 10^9

    return map({a: i + 1 for i, a in enumerate(sorted(set(arr)))}.get, arr)

    rank = {}
    for a in sorted(arr):
        rank.setdefault(a, len(rank) + 1)
    return map(rank.get, arr)
'''
