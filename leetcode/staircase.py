def staircase(n):
    r = []
    for i in range(1, n+1):
        r.append(" "*(n -i) + "#"*i)
    print('\n'.join(r))


staircase(3)
