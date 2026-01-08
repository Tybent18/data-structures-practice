import math

# --------------------
# Jump Search
# --------------------

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

# --------------------
# Interpolation Search
# --------------------

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# --------------------
# Exponential Search
# --------------------

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    return binary_search(arr[:min(i, len(arr))], target)

# --------------------
# Hash Table Search
# --------------------

def hash_search(hash_table, key):
    return hash_table.get(key, None)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# --------------------
# Binary Search Tree
# --------------------

def bst_search(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    elif target < root.value:
        return bst_search(root.left, target)
    else:
        return bst_search(root.right, target)

# --------------------
# Graoh Search (Depth First Search)
# --------------------

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

from collections import deque

# --------------------
# Graph Search (Breath First Search)
# --------------------

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return visited

# --------------------
# A* Search (Heuristic)
# --------------------

import heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(0, start)]
    cost = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return cost[current]

        for neighbor, weight in graph[current]:
            new_cost = cost[current] + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(open_set, (priority, neighbor))

    return None