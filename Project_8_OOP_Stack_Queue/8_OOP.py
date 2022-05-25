# We understand that Python as the queue module
# But we wanted to explore how the data structures worked
# by making our own with Python's list object
from my_library import Stack, Queue

s = Stack()
q = Queue()

# Stack
print("Stack Practice:")
s.push(4)
s.push(3)
s.push(6)

print(s)

print(s.pop())
print(s)
print(s.peek())

print()

# Queue
print("Queue Practice:")
q.add(99)
print(q)
q.add(5)
q.add(9)
print(q)

print(q.remove())
print(q)