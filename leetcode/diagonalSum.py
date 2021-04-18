from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1, d2 = 0, 0
        for i in range(len(mat)):
            d1 += mat[i][i]
            d2 += mat[len(mat)-i-1][i] if len(mat)-i-1 != i else 0 
        t = d1 + d2
        return t

answer = Solution()
input = [[1,2,3],[4,5,6],[7,8,9]]
print(answer.diagonalSum(input))
input = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(answer.diagonalSum(input))
