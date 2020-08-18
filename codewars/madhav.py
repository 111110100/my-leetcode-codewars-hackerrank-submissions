'''
A Madhav array has the following property:

a[0] = a[1] + a[2] = a[3] + a[4] + a[5] = a[6] + a[7] + a[8] + a[9] = ...

Complete the function/method that returns true if the given array is a Madhav array, otherwise it returns false.

Edge cases: An array of length 0 or 1 should not be considered a Madhav array as there is nothing to compare.
'''

def is_madhav_array(arr):
    if len(arr) < 2:
        return False
    i = 1
    k = 2
    while i < len(arr):
        t = 0
        for j in range(k):
            if i > len(arr)-1:
                return False
            t += arr[i]
            i += 1

        if arr[0] != t:
            return False
        else:
            k += 1

    return True

print(is_madhav_array([2, 1, 1]))
print(is_madhav_array([2, 1, 1, 4, -1, -1]))
print(is_madhav_array([3,1,2,3,0]))

'''
def is_madhav_array(arr):
    nTerms = ((1+8*len(arr))**.5-1)/2
    return (len(arr) > 1 and not nTerms%1 and
            len({ sum(arr[int(i*(i+1)//2):int(i*(i+1)//2)+i+1]) for i in range(int(nTerms))}) == 1)

def is_madhav_array(arr):
    p = 1
    c = 2
    while p < len(arr) and arr[0] == sum(arr[p:p + c]):
        p += c
        c += 1      
    return p == len(arr) > 1
'''