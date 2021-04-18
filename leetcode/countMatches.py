class Solution:
    def countMatches(self, items: list, ruleKey: str, ruleValue: str) -> int:
        map = {
            'type': 0,
            'color': 1,
            'name': 2,
        }
        return sum([1 for item in items if item[map[ruleKey]] == ruleValue])

class Solution2:
    def countMatches(self, items: list, ruleKey: str, ruleValue: str) -> int:
        rules = ['type', 'color', 'name']
        return sum((1 for item in items if item[rules.index(ruleKey)] == ruleValue))


answer = Solution2()
input = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
key = 'color'
value = 'silver'
print(answer.countMatches(input, key, value))
key = 'type'
value = 'phone'
print(answer.countMatches(input, key, value))
