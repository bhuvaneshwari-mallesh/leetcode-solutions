# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

**Difficulty:** Easy
**Topics:** Two Pointers, String

## Approach

**Brute force:** pad the shorter string conceptually and loop character by
character using index arithmetic to decide which string to pull from at
each position.

Why it's not meaningfully different here: this problem is inherently
linear either way — there's no asymptotic improvement to be had, just a
cleaner way to handle strings of unequal length.

**Approach used — two pointers, `StringBuilder`:** keep separate pointers
`i` and `j` for `word1` and `word2`. At each step, append `word1[i]` if
`i` is still in bounds, then `word2[j]` if `j` is still in bounds,
advancing whichever pointer was used. Continue while *either* pointer
still has characters left — this is what correctly handles strings of
different lengths, since once one string runs out, only the other keeps
contributing.

Why it works: using `||` (either pointer still valid) instead of `&&`
(both must be valid) in the loop condition means the merge doesn't stop
early when one string is shorter — it just stops appending from the
exhausted string and keeps going with the other, naturally tacking the
longer string's remainder onto the end.

## Complexity

| | Approach used |
|---|---|
| Time | O(n + m) |
| Space | O(n + m) for the result (StringBuilder avoids the extra cost of repeated string concatenation) |

## Key pattern

Two pointers merging two sequences of unequal length, using an "either
still has elements" loop condition — the same shape as the merge step of
merge sort, adapted for strings instead of sorted arrays.
