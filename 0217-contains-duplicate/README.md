# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

**Difficulty:** Easy
**Topics:** Array, Hash Table, Sorting

## Approach

**Brute force:** check every pair `(i, j)` for equality.

Why it's not enough: O(n²).

A simpler alternative: sort the array first, then check only adjacent
elements for equality — O(n log n), better than brute force but not
optimal.

**Optimized — hash set, single pass:** walk the array once. For each
number, check if it's already in a set; if so, a duplicate has been found.
Otherwise, add it and keep going.

Why it works: a set gives O(1) average membership checks, so "have I seen
this before?" is answered instantly at each step instead of requiring a
sort or a nested scan.

## Complexity

| | Brute force | Sort first | Optimized (hash set) |
|---|---|---|---|
| Time | O(n²) | O(n log n) | O(n) |
| Space | O(1) | O(1) (in-place sort) | O(n) |

## Key pattern

Hash set for O(1) "have I seen this?" checks — the simplest member of the
same family as the complement-lookup pattern in Two Sum, applied here to
plain membership instead of pairing.
