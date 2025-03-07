class Stack:
    """
    A custom stack that supports:
      - push(x): Pushes element x onto the stack.
      - pop(): Removes the top element of the stack and returns it.
      - top(): Returns the top element without removing it.
      - getMin(): Returns the smallest element in the stack.
      - getMax(): Returns the largest element in the stack.
    All operations work in O(1) time, and total space is O(n).
    """
    def __init__(self):
        # Initializing an empty list
        self.stack = [] # Each element in self.stack is  gonna be a tuple of the format (actual_value_pushed, current_minimum_value, current_maximum_value)

    def push(self, x):
        if not self.stack:
            # If the stack is empty, x is both min and max
            self.stack.append((x, x, x))
        else:
            # Compare x with the current top's min and max to get the new min and max
            current_min = min(x, self.stack[-1][1])
            current_max = max(x, self.stack[-1][2])
            self.stack.append((x, current_min, current_max))

    def pop(self):
        if not self.stack:
            raise IndexError("pop from an empty stack")
        # pop() returns a tuple, but we only need the value (index 0)
        return self.stack.pop()[0]

    def top(self):
        if not self.stack:
            raise IndexError("top from an empty stack")
        return self.stack[-1][0]  # Retrieve only the value at the top

    def getMin(self):
        if not self.stack:
            raise IndexError("getMin from an empty stack")
        return self.stack[-1][1] # Retrieve min value from the top tuple

    def getMax(self):
        if not self.stack:
            raise IndexError("getMax from an empty stack")
        return self.stack[-1][2]  # Retrieve max value from the top tuple


# --------------------------------------------------------------
# TESTING
# --------------------------------------------------------------
# if __name__ == "__main__":
#     s = Stack()

#     s.push(3) # Stack after push: [(3, 3, 3)]
    
#     print(s.getMin()) # Output: 3 (only element, so min is 3)
#     print(s.getMax()) # Output: 3 (only element, so max is 3)

#     s.push(5) # Stack after push: [(3, 3, 3), (5, 3, 5)]
    
#     print(s.top()) # Output: 5 (top element is now 5)
#     print(s.getMin()) # Output: 3 (min remains 3 as 5 > 3)
#     print(s.getMax()) # Output: 5 (new max is 5)

#     s.push(2) # Stack after push: [(3, 3, 3), (5, 3, 5), (2, 2, 5)]
#     s.push(1) # Stack after push: [(3, 3, 3), (5, 3, 5), (2, 2, 5), (1, 1, 5)]
    
#     print(s.getMin()) # Output: 1 (pushed 1, which is now the min)
#     print(s.getMax()) # Output: 5 (max remains 5)

#     popped_value = s.pop()
#     print(popped_value) # Output: 1 (popped top element, which was 1)
#     print(s.getMin()) # Output: 2 (after popping 1, new min is 2)
#     print(s.getMax()) # Output: 5 (max remains 5)

#     # Pop until empty
#     print(s.pop()) # Output: 2 (popped 2)
#     print(s.pop()) # Output: 5 (popped 5)
#     print(s.pop()) # Output: 3 (popped 3)

#     # Now stack is empty, next line would raise an error
#     print(s.pop()) # Would raise IndexError (stack is empty)

