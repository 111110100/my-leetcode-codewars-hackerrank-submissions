def diagonalDiff(arr):
    d1, d2 = 0, 0
    for i in range(len(arr)):
        d1 += arr[i][i]
        d2 += arr[len(arr)-i-1][i]
    return abs(d1 - d2)

print(diagonalDiff([[1,2,3],[4,5,6],[9,8,9]]))
'''
1 2 3
4 5 6
9 8 9 
'''