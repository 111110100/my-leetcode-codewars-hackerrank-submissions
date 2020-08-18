'''
Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
'''

def reverse_seq(n):
    return [l for l in range(n,0,-1)]

'''
def reverseseq(n):
    return list(range(n, 0, -1))
'''