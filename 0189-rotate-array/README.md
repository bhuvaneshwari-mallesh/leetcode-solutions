# [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

**Difficulty:** Medium
**Topics:** Array, Math, Two Pointers

## Approach

**Brute force:** rotate one step at a time, `k` times — each rotation
shifts every element over by one, which is itself O(n), done `k` times.

Why it's not enough: O(n·k) total, which is bad when `k` is large relative
to `n`.

A simpler-but-costly alternative: build a new array by placing each
element at its rotated index directly — O(n) time but O(n) extra space.

**Optimized — reverse in three steps, in place:** rotating an array right
by `k` is equivalent to:

1. Reverse the whole array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n - k` elements.

(`k` is first reduced via `k % n` to handle `k > n`.)

Why it works: reversing the whole array puts every element in the right
*relative* order for a rotation, but each original half ends up internally
backward. Reversing each half individually un-reverses it back to the
correct internal order — three cheap, in-place reversals replace a full
shift simulation.

## Complexity

| | Brute force (shift k times) | New array | Optimized (3 reversals) |
|---|---|---|---|
| Time | O(n·k) | O(n) | O(n) |
| Space | O(1) | O(n) | O(1) |

## Key pattern

Rotation via reversal — reverse-whole, then reverse-each-part — a
well-known constant-space trick for array/string rotation problems
generally, not just this one.
