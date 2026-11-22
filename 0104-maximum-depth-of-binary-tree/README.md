# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

**Difficulty:** Easy  
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Approach

**Brute force:** We could use a breadth-first search (BFS) level-order traversal, pushing every node onto a queue along with its depth, and track the maximum depth once the queue is empty. While straightforward, this requires extra space to store nodes level by level, which is inefficient for wide trees.

**Optimized:** A recursive depth-first search (DFS) naturally breaks the problem down into subproblems: the maximum depth of any node is simply $1$ plus the maximum of the depths of its left and right subtrees. If a node is null, its depth is $0$. As the call stack unwinds, each node computes its own depth by querying its children.

## Complexity

| | Brute force (BFS) | Optimized (DFS) |
| :--- | :--- | :--- |
| Time | $O(N)$ | $O(N)$ |
| Space | $O(W)$ | $O(H)$ |

*(Where $N$ is the number of nodes, $W$ is the maximum width of the tree, and $H$ is the height of the tree.)*

## Key pattern

This problem demonstrates standard tree recursion (DFS), where solutions bubble up from the base cases to the root. This pattern applies broadly to tree and graph problems involving height, path sums, and structural validation.
