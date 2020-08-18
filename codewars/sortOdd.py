'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''

def sort_array(source_array):
    if len(source_array) != 0:
        n = []
        for v in source_array:
            if v % 2 != 0 and v != 0:
                n.append(v)
        n.sort(reverse=True)
        for i,v in enumerate(source_array):
            if v % 2 != 0 and v != 0:
                source_array[i] = n.pop()
    return source_array 

print(sort_array([5, 3, 2, 8, 1, 4]))

'''
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
'''