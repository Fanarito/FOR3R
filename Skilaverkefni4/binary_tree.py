class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value >= node.value:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = Node(value)
        else:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = Node(value)

    def traverse(self, callback):
        if self.root is None:
            return

        self._traverse(self.root.left, callback)
        callback(self.root.value)
        self._traverse(self.root.right, callback)

    def _traverse(self, node, callback):
        if node is None:
            return

        self._traverse(node.left, callback)
        callback(node.value)
        self._traverse(node.right, callback)

    def search(self, value):
        if self.root is None:
            return None

        if value == self.root.value:
            return self.root
        elif value > self.root.value:
            return self._search(value, self.root.right)
        else:
            return self._search(value, self.root.left)

    def _search(self, value, node):
        if node is None:
            return None

        if value == node.value:
            return node
        elif value > node.value:
            return self._search(value, node.right)
        else:
            return self._search(value, node.left)

    def maximum(self):
        if self.root is None:
            return None
        elif self.root.right is None:
            return self.root
        else:
            return self._maximum(self.root.right)

    def _maximum(self, node):
        if node.right is None:
            return node
        else:
            return self._maximum(node.right)

    def minimum(self):
        if self.root is None:
            return None
        elif self.root.left is None:
            return self.root
        else:
            return self._minimum(self.root.left)

    def _minimum(self, node):
        if node.left is None:
            return node
        else:
            return self._minimum(node.left)

    def delete(self):
        self.root = None

thing = Tree()
thing.insert(5)
thing.insert(4)
thing.insert(3)
thing.insert(2)
thing.insert(1)
thing.insert(6)
thing.insert(7)
thing.insert(8)
thing.insert(9)
thing.insert(10)
thing.traverse(print)
print(thing.search(10))
print(thing.maximum().value)
print(thing.minimum().value)
