def xmastree(n):
    r = []
    for i in range(0, n+1):
        r.append(" "*(n-i) + "#"*(i+1) + "#"*(i+1-1))
    print('\n'.join(r))


xmastree(6)
