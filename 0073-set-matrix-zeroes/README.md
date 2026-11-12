# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

**Difficulty:** Medium
**Topics:** Array, Hash Table, Matrix

## Approach

**Brute force:** scan the matrix for zeros, record their row/column
indices in a separate set, then do a second pass zeroing out every cell
whose row or column appears in that set.

Why it's not ideal: O(n·m) extra space for the row/column sets, when the
problem rewards doing it in O(1) extra space.

**Optimized — use the matrix's own first row and column as markers:**
instead of a separate set, use `matrix[i][0]` and `matrix[0][j]` themselves
to record "row i has a zero" / "column j has a zero." A separate flag
(`c0`) tracks whether the first column itself needs zeroing, since
`matrix[0][0]` is shared between the row-marker and column-marker roles.

Steps:
1. Scan the matrix; whenever a zero is found at `(i, j)`, mark
   `matrix[i][0] = 0` and `matrix[0][j] = 0` (using `c0` instead when
   `j == 0`, to avoid clobbering the shared corner cell).
2. Second pass (skipping row 0 and column 0): zero out any cell whose row
   marker or column marker is set.
3. Handle row 0 and column 0 themselves last, using `matrix[0][0]` and
   `c0`.

Why it works: the first row and column have exactly n + m cells — plenty
of room to store "has a zero" flags for all n rows and m columns, so no
extra data structure is needed; the matrix becomes its own scratch space.

## Complexity

| | Brute force (extra sets) | Optimized (in-place markers) |
|---|---|---|
| Time | O(n·m) | O(n·m) |
| Space | O(n + m) | O(1) extra |

## Key pattern

Using part of the existing input as scratch space instead of allocating a
new structure — a recurring trick for "reduce extra space" matrix/array
follow-ups.
