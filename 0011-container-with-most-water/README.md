# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Greedy

## Approach

**Brute force:** try every pair of lines `(i, j)`, compute the area
`min(height[i], height[j]) * (j - i)`, and keep the max.

Why it's not enough: O(n²) pairs to check.

**Optimized — two pointers from both ends:** start `left` at index 0 and
`right` at the last index. At each step compute the area between them,
then move whichever pointer points at the *shorter* line inward.

Why it works (the non-obvious part): the area is capped by the shorter of
the two lines. If you move the pointer at the *taller* line instead, the
width only shrinks and the limiting height can't improve — the area can
only get worse. Moving the shorter line's pointer is the only move that
has a chance of finding a taller line and a bigger area, so it's safe to
discard every pairing with the shorter line without checking them
individually.

## Complexity

| | Brute force | Optimized |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |

## Key pattern

Two pointers closing in from both ends, with a greedy "always move the
worse side" rule — common whenever the answer depends on a min/max of two
boundaries and width between them.
