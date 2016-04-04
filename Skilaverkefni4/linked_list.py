class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add(self, value):
        new_node = Node(value, next=self.cur_node)
        self.cur_node = new_node

    def travel(self, callback):
        node = self.cur_node
        while node:
            callback(node.value)
            node = node.next

    def get(self, index):
        count = 0
        node = self.cur_node
        while index > count:
            node = node.next
            count += 1
        return node

    def head(self):
        return self.cur_node

    def foot(self):
        node = self.cur_node
        while node.next:
            node = node.next
        return node

    def search(self, value):
        index = 0
        node = self.cur_node
        while node.value != value:
            if node is None:
                return -1
            index += 1
            node = node.next
        return index

    def delete(self, value):
        node = self.cur_node
        prev_node = None
        while node:
            if node.value == value and prev_node is None and node.next is None:
                cur_node = None
            elif node.value == value and node.next is not None:
                prev_node.next = node.next
            elif node.value == value:
                prev_node.next = None

            prev_node = node
            node = node.next

    def delete_index(self, index):
        count = 0
        node = self.cur_node
        prev_node = None
        while index > count:
            prev_node = node
            node = node.next
            count += 1
        if prev_node is not None and node.next is not None:
            prev_node.next = node.next
        elif prev_node is None:
            self.cur_node = node.next
        elif node.next is None:
            prev_node.next = None

    def clear(self):
        self.cur_node = None


thing = LinkedList()
thing.add(5)
thing.add(10)
thing.add(20)
thing.travel(print)
print(thing.get(0).value)
print(thing.head().value)
print(thing.foot().value)
print(thing.search(5))
print("----")
thing.delete(5)
thing.delete_index(0)
thing.travel(print)
thing.clear()
print("----")
thing.travel(print)
