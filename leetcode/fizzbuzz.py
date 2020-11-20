class Solution:
    def fizzBuzz(self, n):
        return ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, n+1)]

answer = Solution()
print(answer.fizzBuzz(15))

'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

class Solution:
    def fizzBuzz(self, n):
        l = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                l.append('FizzBuzz')
            elif i % 3 == 0:
                l.append('Fizz')
            elif i % 5 == 0:
                l.append('Buzz')
            else:
                l.append(str(i))
        return l

        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

        return [(not i%3)*"Fizz" + (not i%5)*"Buzz" or str(i) for i in range(1, n+1)]

        return ['FizzBuzz' if i%15 == 0 else 'Buzz' if i%5 == 0 else 'Fizz' if i%3 == 0 else str(i) for i in range(1,n+1)]
'''