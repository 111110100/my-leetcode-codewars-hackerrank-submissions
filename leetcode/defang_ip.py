import re

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub('\.', '[.]', address)

ip = Solution()
print(ip.defangIPaddr("1.1.1.1"))

# this solution appears to be faster than regular str.replace()
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''
