'''
Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)

Matrix = array of n length whose elements are n length arrays of integers.

3x3 example:

sum_diagonals[
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7

'''

def sum_diagonals(matrix):
    x = 0
    for i in range(len(matrix)):
        x += matrix[i][i]
        x += matrix[len(matrix)-i-1][i]
    return x

'''
def sum_diagonals(a):
    return sum(a[i][i] + a[i][-i-1] for i in range(len(a)))

def sum_diagonals(matrix):
    return sum(row[i] + row[-i - 1] for i, row in enumerate(matrix))
'''