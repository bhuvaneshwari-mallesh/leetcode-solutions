# [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)

**Difficulty:** Easy
**Topics:** Array, Simulation

## Approach

This is about as direct as a problem gets — there's no meaningfully
slower "brute force" distinct from the solution itself; the task is
literally "build an array that is `nums` followed by `nums` again."

**Approach used — single pass, write to both halves:** create a new array
of size `2n`. In one pass over `nums`, write each element to both its
original position `i` and its mirrored position `i + n` at the same time.

Why it works: the output is defined as `nums + nums`, so placing each
element into both halves in the same loop iteration avoids a second
separate pass — same total work, just done together rather than
sequentially.

## Complexity

| | Approach used |
|---|---|
| Time | O(n) |
| Space | O(n) extra (the result array; required by the problem, not avoidable) |

## Key pattern

Not much of a generalizable pattern here beyond "when the output has
repeated structure from the input, write to both positions in a single
pass instead of two separate loops" — a small efficiency habit more than
a reusable algorithmic idea.
