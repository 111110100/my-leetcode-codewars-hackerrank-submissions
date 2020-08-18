def staircase(n):
    for i in range(1, n + 1):
        print(" "*(n - i)+"#"*i)


print(staircase(6))