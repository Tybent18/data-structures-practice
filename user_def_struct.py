class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)  # O(1) instead of O(n)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def print_stack(self):
        print(self.items[::-1])  # Top element on the left

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()  # O(1)

    def print_queue(self):
        print(list(self.items))

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def get_last_node(self):
        if not self.head:
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.data

    def is_empty(self):
        return self.head is None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" => ")
            curr = curr.next
        print("None")

class Graph:
    def __init__(self, size):
        self.size = size
        self.adj = [[0] * size for _ in range(size)]

    def add_edge(self, orig, dest):
        if not (0 <= orig < self.size) or not (0 <= dest < self.size):
            print("Invalid edge")
            return
        self.adj[orig][dest] = 1
        self.adj[dest][orig] = 1

    def remove_edge(self, orig, dest):
        if not (0 <= orig < self.size) or not (0 <= dest < self.size):
            print("Invalid edge")
            return
        self.adj[orig][dest] = 0
        self.adj[dest][orig] = 0

    def display(self):
        for row in self.adj:
            print(" ".join(map(str, row)))

class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_tree(root, space=0, position=None):
    COUNT = 3
    if root is None:
        return

    space += COUNT
    print_tree(root.right, space, "R")

    print(" " * (space - COUNT), end="")
    if position == "R":
        print("/ ", root.data)
    elif position == "L":
        print("\\ ", root.data)
    else:
        print(root.data)

    print_tree(root.left, space, "L")

class HashTable:
    def __init__(self, size=127):
        self.size = size
        self.table = [None] * size

    def _hash(self, value):
        return sum(ord(c) for c in value) % self.size

    def insert(self, value):
        h = self._hash(value)
        self.table[h] = value  # naive, no collision handling

    def search(self, value):
        h = self._hash(value)
        if self.table[h] == value:
            return h
        return None

    def remove(self, value):
        h = self._hash(value)
        if self.table[h] == value:
            self.table[h] = None
            print(f"Element {value} deleted")
        else:
            print(f"No element found with value {value}")
