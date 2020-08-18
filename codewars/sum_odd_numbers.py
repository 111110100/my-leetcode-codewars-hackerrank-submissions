'''
sum of odd
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
'''

def row_sum_odd_numbers(n):
    s,e,x = 2,1,n
    while x > 1:
        e += s
        s += 2
        x -= 1
    f,u = n,0
    while f > 0:
        u += e 
        e += 2
        f -= 1
    return u 

print(row_sum_odd_numbers(3)) # 7 

'''
def row_sum_odd_numbers(n):
    return n ** 3

def row_sum_odd_numbers(n):
    return n*n*n

def row_sum_odd_numbers(n):
    return pow(n, 3)
'''