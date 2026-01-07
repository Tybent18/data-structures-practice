# --------------------
# Depth-First Search
# --------------------
def dfs(graph, start):
    visited = []
    
    def _dfs(vertex):
        visited.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return visited


# --------------------
# Binary Search
# --------------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# --------------------
# Linear Search
# --------------------
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# --------------------
# Binary Search Tree
# --------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bst_search(root, target):
    if root is None:
        return None

    if root.data == target:
        return root
    elif target < root.data:
        return bst_search(root.left, target)
    else:
        return bst_search(root.right, target)


def bst_insert(root, node):
    if root is None:
        return node

    if node.data < root.data:
        root.left = bst_insert(root.left, node)
    else:
        root.right = bst_insert(root.right, node)

    return root