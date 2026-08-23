---
name: data-structures-algorithms
description: Use when solving algorithmic problems, optimizing code, or choosing the right data structure for performance.
version: 1.0.0
author: Kintama
license: MIT
metadata:
  hermes:
    tags: [algorithms, data-structures, complexity, optimization, problem-solving]
    related_skills: [performance-optimization, systematic-debugging]
---

# Data Structures & Algorithms

## Complexity Analysis
- Always analyze time AND space complexity
- Big O: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- Amortized analysis for dynamic structures

## Core Data Structures

| Structure | Access | Search | Insert | Delete | Use When |
|-----------|--------|--------|--------|--------|----------|
| Array | O(1) | O(n) | O(n) | O(n) | Random access, cache locality |
| Hash Map | O(1) | O(1) | O(1) | O(1) | Key-value lookup |
| Linked List | O(n) | O(n) | O(1) | O(1) | Frequent insert/delete |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) | Sorted data |
| Heap | O(1) top | O(n) | O(log n) | O(log n) | Priority queue |
| Graph | - | O(V+E) | O(1) | O(E) | Relationships, paths |

## Algorithm Patterns
- **Two Pointers** — sorted arrays, palindromes
- **Sliding Window** — subarray/substring problems
- **Binary Search** — sorted data, search space reduction
- **DFS/BFS** — tree/graph traversal
- **Dynamic Programming** — overlapping subproblems, optimal substructure
- **Greedy** — locally optimal choices lead to global optimum
- **Divide & Conquer** — merge sort, quick sort

## Choosing the Right Structure
1. Need O(1) lookup? → Hash Map
2. Need sorted order? → BST / Sorted Array
3. Need LIFO? → Stack
4. Need FIFO? → Queue
5. Need priority? → Heap
6. Need relationships? → Graph
7. Need prefix search? → Trie
