# TASK1
def clear(self):
    current = self.head
    while current is not None:
        temp = current.next
        del current.data
        current = temp
    self.head = None
    self.size = 0


# TASK2
def get_data(self, data):
    if self.head is None:
        return None

    current = self.head
    while current is not None:
        if current.data == data:
            return current
        current = current.next

    return None


# TASK3
class SLLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def insert_node(self, prev_node_data, new_node_data):
    new_node = SLLNode(new_node_data)
    current = self.head
    while current is not None:
        if current.data == prev_node_data:
            new_node.next = current.next
            current.next = new_node
            self.size += 1
            return
        else:
            current = current.next
    self.append(new_node_data)


# TASK4
def delete_node(self, data):
    current = self.head
    prev_node = None
    found = False
    while current and not found:
        if current.data == data:
            found = True
        else:
            prev_node = current
            current = current.next

    if found:
        if prev_node is None:
            self.head = current.next
        else:
            prev_node.next = current.next
        self.size -= 1


# TASK5
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DLLNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_node(self, prev_node_data, new_node_data):
        current = self.head
        while current is not None:
            if current.data == prev_node_data:
                new_node = DLLNode(new_node_data)
                new_node.prev = current
                new_node.next = current.next
                if current.next is None:
                    self.tail = new_node
                else:
                    current.next.prev = new_node
                current.next = new_node
                self.size += 1
                return True
            current = current.next
        return False

    def delete_node(self, data):
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return True

        current = self.head.next
        while current is not None and current.data != data:
            current = current.next

        if current is not None:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            else:
                self.tail = current.prev
            self.size -= 1
            return True

        return False

    def get_data(self):
        current = self.head
        data = []
        while current is not None:
            data.append(current.data)
            current = current.next
        return data

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0


# TASK6
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class MyStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    def top(self):
        if self.tail is None:
            return None
        return self.tail.data

    def size(self):
        return self.size


# TASK7

class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def show_left(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def show_right(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
