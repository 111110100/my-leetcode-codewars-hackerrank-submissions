import re

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub('\.', '[.]', address)

ip = Solution()
print(ip.defangIPaddr("1.1.1.1"))

# this solution appears to be faster than regular str.replace()
