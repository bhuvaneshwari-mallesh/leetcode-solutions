# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

**Difficulty:** Easy
**Topics:** Array, String, Trie

## Approach

**Brute force:** compare characters column by column across all strings
(check index 0 of every string, then index 1, etc.) until a mismatch or a
string runs out.

Why it's not ideal: still has to be written carefully to avoid index errors,
and it's not meaningfully different in complexity from the approach actually
used — the real brute force here mostly differs in style, not asymptotic cost.

**Optimized — shrink-the-prefix approach:** start by assuming the first
string is the whole answer (`prefix = strs[0]`). For every other word, while
the word doesn't start with `prefix`, chop one character off the end of
`prefix`. By the time every word has been checked, whatever's left of
`prefix` is guaranteed to be a common prefix of all of them.

Why it works: the common prefix can only ever be as long as the shortest
match found so far, so repeatedly trimming the current candidate down
against each word converges on the true shared prefix without ever needing
to compare character-by-character by hand.

## Complexity

| | Approach used |
|---|---|
| Time | O(S) where S = total characters across all strings (worst case) |
| Space | O(1) extra (prefix slicing aside) |

## Key pattern

Shrink-a-candidate-against-the-data — instead of building the answer up
char by char, start with an over-optimistic guess and narrow it down until
it's valid against every input.
