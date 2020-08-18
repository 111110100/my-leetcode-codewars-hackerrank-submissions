def minMaxSum(arr):
    res = [sum(arr) - arr[i] for i in range(len(arr))]
    print(f'{min(res)} {max(res)}')

print(minMaxSum([1,2,3,4,5]))