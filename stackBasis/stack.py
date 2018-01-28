
class Stack:

    def __init__(self):
        self.items = []

    # Judge the stack is empty or not
    def isEmpty(self):
        return self.items == []

    # Add an item into the stack
    def push(self, item):
        self.items.append(item)

    # Delete the top item
    def pop(self):
        return self.items.pop()

    # Back to the top of the stack
    def peek(self):
        return self.items[len(self.items) - 1]

    # Get the size of the stack
    def size(self):
        return len(self.items)
