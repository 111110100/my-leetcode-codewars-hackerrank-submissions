a = [[11, 2 ,4], [4, 5, 6], [10, 8, -12]]

d1, d2 = 0, 0

print(a)
for i in range(len(a)):
    d1 += a[i][i]
    d2 += a[len(a)-i-1][i]
    #print(a[i][i])
    #print(a[len(a)-i-1][i])

print(abs(d1-d2))
