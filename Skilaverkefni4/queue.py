class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        return self.queue.pop(0)

    def clear(self):
        self.queue = []

thing = Queue()
thing.push(1)
thing.push(2)
thing.push(3)
print(thing.pop())
print(thing.pop())
print(thing.pop())
