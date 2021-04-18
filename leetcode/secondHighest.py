#%%
import re

class Solution:
    def secondHighest(self, s: str) -> int:
        l = sorted(list(set(list(''.join(re.split('[a-zA-Z]', s))))))
        if len(l) <= 1:
            return -1
        return int(l[-2]) 

class Solution2:
    def secondHighest(self, s: str) -> int:
        t = set()
        for i in s:
            if '0'<=i<='9':
                t.add(int(i))
        if len(t) > 1:
            return sorted(list(t))[-2]
        return -1

answer = Solution()
print(answer.secondHighest("abc1111"))

#%%
import re
sorted(list(set(list(''.join(re.split('[a-zA-Z]', 'dfa412321afd1'))))))[-1]
#%%
