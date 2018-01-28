from stackBasis.stack import Stack

s = Stack()

# Is the stack empty or not
print(s.isEmpty())

# Insert items into stack s
s.push(4)
s.push('dog')

# Get the top item
print(s.peek())

# Get the size of stack s
print(s.size())

print(s.isEmpty())

# Delete top item
print(s.pop())

print(s.peek())



