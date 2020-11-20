class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)

answer = Solution()
print(answer.removeOuterParentheses("(()())(())"))
print(answer.removeOuterParentheses("(()())(())(()(()))"))

'''
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string

def removeOuterParentheses(self, S):
	res = []
	balance = 0
	i = 0
	for j in range(len(S)):
		if S[j] == "(":
			balance += 1
		elif S[j] == ")":
			balance -= 1
		if balance == 0:
			res.append(S[i+1:j])
			i = j+1
	return "".join(res)

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        stack = []
        
        # basket is used to store previous value
        basket = ''
        
        for p in S:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
            basket += p
            
            # if the stack is empty it means we have a valid
            # decomposition. remove the outer parentheses
            # and put it in the result/res. make sure to
            # clean up the basket though!
            if not stack:
                res += basket[1:-1]
                basket = ''
                
        return res
'''
