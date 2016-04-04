class Queue:
    def __init__(self):
        self.queue = []

    def push(self, priority, value):
        if not self.queue:
            self.queue.append([priority, value])
        else:
            idx = 0
            while self.queue[idx][0] > priority:
                idx += 1
            self.queue.insert(idx, [priority, value])

    def pop(self):
        return self.queue.pop(0)[1]

    def clear(self):
        self.queue = []

thing = Queue()
thing.push(1, 1)
thing.push(2, 2)
thing.push(3, 3)
thing.push(2, 4)
thing.push(1, 5)
print(thing.pop())
print(thing.pop())
print(thing.pop())
print(thing.pop())
print(thing.pop())

