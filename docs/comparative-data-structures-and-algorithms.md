# Comparative Data Structures and Algorithms: Implementations, Complexity, and Learning Evidence

**T. R. Bentley**  
Repository-grounded technical report | September 2026  
Repository: Tybent18/data-structures-practice

> [Download the publication PDF](comparative-data-structures-and-algorithms.pdf) · [Repository README](../README.md)

## Abstract

This report organizes a multi-language practice collection around two evidence classes: data representation and algorithmic transformation. Linked lists, stacks, trees, structures, searching, sorting, and recursion are mapped to their source artifacts. Complexity expectations are stated as analytical baselines rather than benchmark results, and a measurement plan is defined for future empirical comparison.

## Scope

Foundational structures and algorithms implemented primarily in Python and C.

Claims are limited to named repository artifacts. Proposed tests, benchmarks, integrations, and research directions are future work—not reported results.

## Repository evidence map

| Cluster | Artifacts | Interpretation |
| --- | --- | --- |
| Linear structures | `linked_list.c, stack.c` | Pointer-linked storage and last-in-first-out behavior. |
| Hierarchical structures | `binary_tree.c` | Tree representation and traversal foundations. |
| Representation | `struct.c, user_def_struct.py` | Contrasts explicit C records with Python-defined structures. |
| Search | `search.py, expand_search.py` | Search strategies and extension exercises. |
| Sort and recursion | `sort.py, expand_sort.py, recursion.py` | Ordering transformations and recursive decomposition. |

## Technical questions

- How do language choices change implementation detail while preserving abstract behavior?
- Which operations dominate time and auxiliary-space costs?
- How can correctness be separated from performance measurement?

## Reproducible inspection protocol

A reviewer should clone the repository, record the commit SHA and toolchain versions, inspect each mapped artifact, execute only examples with declared entry points, preserve outputs and errors, and compare observations with stated expectations. A deliberate debugging failure is evidence only when its expected failure class is declared in advance.

## Evidence maturity

| Level | Meaning |
| --- | --- |
| E0 | Artifact listed |
| E1 | Intended behavior described |
| E2 | Environment, command, and output recorded |
| E3 | Repeatable behavioral tests included |
| E4 | Frozen data supports a bounded comparison |

## Limitations

- Complexity statements are theoretical expectations, not measured timings.
- Implementations do not yet share a unified test corpus.
- The collection is educational and not optimized as a production library.

## Development roadmap

- Add parameterized correctness tests.
- Create a frozen benchmark dataset across input sizes.
- Record operation counts and wall-clock distributions separately.

## Portfolio role

This repository belongs to the cumulative sequence **Foundations & Algorithms → Data Structures Practice → OOP Concepts → Math for Computing → Practical Utilities**. Advanced repositories carry the stronger systems and empirical-research claims.

## Conclusion

The repository is most credible when each claim points to inspectable code and future measurements can be added without rewriting history. Sophistication comes from traceability, not inflated labels.
