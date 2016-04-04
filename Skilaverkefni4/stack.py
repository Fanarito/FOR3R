class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

thing = Stack()
thing.push(1)
thing.push(2)
thing.push(3)
print(thing.pop())
print(thing.pop())
print(thing.pop())
