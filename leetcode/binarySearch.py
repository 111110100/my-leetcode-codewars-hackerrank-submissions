class Solution:
    def binarySearch(self, numbers, target):
        numbers = sorted(numbers)
        found = False
        bottom = 0
        top = len(numbers) - 1
        while bottom <= top and not found:
            middle = (bottom + top) // 2
            if numbers[middle] == target:
                found = True
                return numbers[middle] 
            elif numbers[middle] < target:
                bottom = middle + 1
            else:
                top = middle - 1
        return False


answer = Solution()
print(answer.binarySearch([3, 11, 4, 1, 43, 21, 13, 7], 13))
