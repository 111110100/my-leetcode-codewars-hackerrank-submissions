class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)
        

class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, val: int) -> None:
        if self.stack:
            m = min(val, self.stack[-1][0])
            self.stack.append((m, val))
        else:
            self.stack.append((val, val))
        return

    def pop(self) -> None:
        self.stack.pop()[1]
        return

    def top(self) -> int:
        return self.stack[-1][1]
        
    def getMin(self) -> int:
        return self.stack[-1][0]


class MinStack3(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        self.min = float("inf")

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if (not self.lst):
            self.lst.append(val)
            self.min = val
        else:
            if (val < self.min):
                self.min = val
            self.lst.append(val)

    def pop(self):
        """
        :rtype: None
        """
        result = self.lst[-1]
        self.lst = self.lst[:-1]
        if (result == self.min and self.lst):
            self.min = min(self.lst)
        return result


    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


class MinStack4:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
"""
MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
"""
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

answer = MinStack4()
answer.push(-2)
answer.push(0)
answer.push(-1)
answer.getMin() # return -3
answer.pop()
answer.top()    # return 0
answer.getMin() # return -2
print(answer.stack)

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-2^31 <= val <= 2^31 - 1

Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
