# Data Structures Practice

Classic data structures, searching techniques, sorting algorithms, and recursion exercises implemented across Python and C.

## What this repository demonstrates

- linked structures, stacks, and binary trees
- linear and binary searching
- common sorting strategies
- recursion and structured problem decomposition
- comparisons between language-level implementations

## Repository map

### Structures

| File | Focus |
| --- | --- |
| [`linked_list.c`](linked_list.c) | Linked-list construction and traversal |
| [`stack.c`](stack.c) | Stack operations |
| [`binary_tree.c`](binary_tree.c) | Binary-tree representation |
| [`struct.c`](struct.c) | C structures |
| [`user_def_struct.py`](user_def_struct.py) | User-defined structures in Python |

### Algorithms

| File | Focus |
| --- | --- |
| [`search.py`](search.py) | Core search routines |
| [`expand_search.py`](expand_search.py) | Extended search exercises |
| [`sort.py`](sort.py) | Core sorting routines |
| [`expand_sort.py`](expand_sort.py) | Extended sorting exercises |
| [`recursion.py`](recursion.py) | Recursive problem solving |

## Run an example

```bash
python search.py
python sort.py
gcc -Wall -Wextra -pedantic linked_list.c -o linked_list
./linked_list
```

## Learning goals

- understand how each structure stores and retrieves data;
- reason about time and space costs;
- compare iterative and recursive solutions;
- practice translating an algorithm between languages.

## Foundation portfolio

This repository is part of a five-repository learning path:

1. [Foundations & Algorithms](https://github.com/Tybent18/foundations-algorithms)
2. [Data Structures Practice](https://github.com/Tybent18/data-structures-practice)
3. [OOP Concepts](https://github.com/Tybent18/oop-concepts)
4. [Math for Computing](https://github.com/Tybent18/math-for-computing)
5. [Practical Utilities](https://github.com/Tybent18/practical-utilities)

## Status

Foundational implementations complete; additional tests, complexity notes, and language comparisons are natural next steps.

## License

[MIT](LICENSE)
