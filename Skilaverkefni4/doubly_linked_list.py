class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.last = None
        self.current = None

    def head(self):
        return self.current

    def foot(self):
        return self.last

    def add(self, value):
        if self.current is None:
            newNode = Node(value)
            self.current = newNode
            self.last = newNode
        else:
            newNode = Node(value)
            self.current.prev = newNode
            newNode.next = self.current
            self.current = newNode

    def traverse(self, callback):
        node = self.current
        while node is not None:
            callback(node.value)
            node = node.next

    def traverse_backwards(self, callback):
        node = self.last
        while node is not None:
            callback(node.value)
            node = node.prev

    def get(self, index):
        count = 0
        node = self.current
        while count < index:
            if node.next is None:
                return None
            count += 1
            node = node.next
        return node

    def search(self, value):
        count = 0
        node = self.current
        while node.value != value:
            if node.next is None:
                return -1
            node = node.next
            count += 1
        return count

    def delete(self, value):
        node = self.current
        while node:
            if node.value == value:
                if node.next and node.prev:
                    # wow hvað þetta er ljótt
                    node.next.prev = node.prev.prev.next
                    node.prev.next = node.next
                elif node.next and node.prev is None:
                    node.next.prev = None
                    self.current = node.next
                elif node.prev and node.next is None:
                    node.prev.next = None
                    self.last = node.prev
            node = node.next

    def delete_index(self, index):
        count = 0
        node = self.current
        while node:
            if node.next is None:
                return

            if count == index:
                if node.next and node.prev:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                elif node.next and node.prev is None:
                    node.next.prev = None
                    self.current = node.next
                elif node.prev and node.next is None:
                    node.prev.next = None
                    self.last = node.prev
            count += 1
            node = node.next

    def clear(self):
        self.last = None
        self.current = None


thing = DoublyLinkedList()
thing.add(1)
thing.add(2)
thing.add(3)
thing.add(4)
thing.delete_index(0)
thing.traverse(print)
thing.traverse_backwards(print)
