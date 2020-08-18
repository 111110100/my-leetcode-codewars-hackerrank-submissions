def buildTower(n):
    for i in range(1, n + 1):
        print(' '*(n - i)+"*"*(i ** i)+' '*(n + i))

print(buildTower(3))