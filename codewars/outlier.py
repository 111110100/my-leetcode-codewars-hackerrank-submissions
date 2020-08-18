'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
FAIL1:
def find_outlier(integers):
    p = sum(integers) % 2
    l = integers + [[],[0],[0,0]][(len(integers) % 3) - 1]
    chunk_size = 3
    for i in range(0, len(l), chunk_size):
        chunk = l[i:i+chunk_size]
        if sum(chunk) % 2 == p:
            for v in chunk:
                if v % 2 == p:
                    return v

    return None
'''

def find_outlier(integers):
    p = 0
    for i in range(0, 3):
        p += integers[(i)] % 2 
    p = 1 if p == 0 or p == 1 else 0
    for i in integers:
        if i % 2 == p:
            return i
    return None

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([17, 6, 8, 10, 6, 12, 24, 36]))

'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier(nums):
  base_parity = sum( x%2 for x in nums[:3] ) // 2
  for i in range(len(nums)):
    if nums[i] % 2 != base_parity:
      return nums[i]

def find_outlier(integers):
    assert len(integers) >= 3
    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False

def find_outlier(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]
'''