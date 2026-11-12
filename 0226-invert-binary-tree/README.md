# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

**Difficulty:** Easy
**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Approach

**Brute force:** there isn't really a meaningfully different "slower"
approach here — inverting a tree inherently requires visiting every node
once, however it's traversed (DFS or BFS). The real decision is
recursive vs iterative, not brute force vs optimized.

**Approach used — recursive DFS:**

1. Base case: an empty node (`None`) has nothing to invert — return `None`.
2. Swap the node's `left` and `right` children.
3. Recursively invert the (now-swapped) left subtree, then the right
   subtree.
4. Return the node itself.

Why it works: inverting a tree just means every node's children are
swapped, all the way down. Recursion naturally expresses "do this to the
current node, then let the same logic handle each subtree" — each call
only has to worry about its own node and trust that the recursive calls
correctly handle everything below it.

An equivalent **iterative BFS version** (using a queue, swapping children
as each node is dequeued and pushing the children for later processing)
would do the same work with the same complexity — useful to know as an
alternative if recursion depth ever becomes a concern on very unbalanced
trees.

## Complexity

| | Recursive DFS (used) |
|---|---|
| Time | O(n) — every node visited once |
| Space | O(h) — recursion stack, h = tree height (O(n) worst case on a skewed tree, O(log n) on a balanced one) |

## Key pattern

Recursive tree traversal where each node's job is local (swap two
children) and the recursion handles propagating that job through the rest
of the structure — the template for most "transform every node" tree
problems.
