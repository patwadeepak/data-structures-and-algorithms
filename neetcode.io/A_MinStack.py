class MinStack:
    """
    This is a simple stack implementation that does not track the minimum value efficiently.
    So, all operations are O(1) except for getMin, which is O(n).
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minValue = self.stack[0]
        for num in self.stack:
            minValue = min(minValue, num)
        return minValue


class MinStack2:
    """
    This pattern is commonly called the "auxiliary stack" or "support stack" technique.
    At every step, minStack mirrors the main stack in size, 
    but each entry is the minimum value up to that point.
    So, after any number of pushes and pops, the top of minStack is always the minimum of the current stack.
    All operations are O(1) in time complexity. But it uses O(n) space complexity.
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(val if self.minStack[-1] > val else self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

class MinStack3:
    """
    This is a space-optimized minimum tracking technique using difference encoding.
    It's less common than the auxiliary stack method, but achieves the same goal with less memory.
    The key idea is to encode information about the minimum directly into the stack values,
    allowing you to reconstruct the minimum as needed. 
    All operations are O(1) in time complexity, and it uses O(1) space complexity.
    """
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min