# --------------------
# Factorial
# --------------------

def factorial(n):
    if n <= 1:        # base case
        return 1
    return n * factorial(n-1)

# Example usage:
num = 5
print(f"Factorial of {num} is {factorial(num)}")

# --------------------
# Fibonacci
# --------------------

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# --------------------
# Array Sum
# --------------------

def sum_array(arr):
    if not arr:       # base case: empty array
        return 0
    return arr[0] + sum_array(arr[1:])  # first element + sum of the rest

# Example usage:
arr = [1, 2, 3, 4, 5]
print(f"Sum of {arr} is {sum_array(arr)}")

# --------------------
# Binary Search
# --------------------

def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid+1, r, x)
    return -1

# --------------------
# Tree Traversal
# --------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# --------------------
# Backtracking
# --------------------

def solveMaze(maze, x, y, solution):
    if x == len(maze)-1 and y == len(maze[0])-1:  # goal reached
        solution[x][y] = 1
        return True
    if isSafe(maze, x, y):
        solution[x][y] = 1
        if solveMaze(maze, x+1, y, solution):
            return True
        if solveMaze(maze, x, y+1, solution):
            return True
        solution[x][y] = 0  # backtrack
        return False
    return False

# --------------------
# Divideand Conquer
# --------------------

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# --------------------
# Memoization Recursion
# --------------------

memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# --------------------
# Graph Recursion
# --------------------

def dfs(graph, node, visited=set()):
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)