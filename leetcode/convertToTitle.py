class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title = alphabet[remainder] + title
        return title 

class Solution2:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            title = alphabet[columnNumber % 26] + title
            columnNumber //= 26
        return title

answer = Solution2()
print(answer.convertToTitle(1) == "A")
print(answer.convertToTitle(2147483647) == "FXSHRXW")

```
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"


Constraints:

1 <= columnNumber <= 2^31 - 1
```
