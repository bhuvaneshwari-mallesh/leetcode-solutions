# [48. Rotate Image](https://leetcode.com/problems/rotate-image/)

**Difficulty:** Medium
**Topics:** Array, Math, Matrix

## Approach

**Brute force:** build a brand-new matrix, and for each cell `(i, j)` in
the original, place it at its rotated position `(j, n-1-i)` in the new
matrix, then copy the new matrix back over the old one.

Why it's not ideal: the problem asks for an **in-place** rotation —
O(n²) extra space for a second matrix isn't allowed.

**Optimized — transpose, then reverse each row:** two simple, well-known
matrix operations chained together:

1. **Transpose** the matrix in place (swap `matrix[i][j]` with
   `matrix[j][i]` for every `j > i`) — this flips it across the main
   diagonal.
2. **Reverse each row** — this completes the 90° clockwise rotation.

Why it works: a 90° clockwise rotation is mathematically equivalent to a
transpose followed by a horizontal flip. Both steps can be done in place
with simple swaps, so no extra matrix is ever needed.

## Complexity

| | Brute force (new matrix) | Optimized (transpose + reverse) |
|---|---|---|
| Time | O(n²) | O(n²) |
| Space | O(n²) | O(1) extra |

## Key pattern

Decomposing a geometric transformation (rotation) into two simpler,
well-known in-place operations (transpose, reverse) — worth remembering
for other matrix-manipulation problems (reflections, other rotation
angles).
