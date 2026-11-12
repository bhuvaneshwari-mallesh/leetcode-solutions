# [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

**Difficulty:** Easy
**Topics:** Two Pointers, String, Dynamic Programming

## Approach

**Brute force:** for each character of `s`, search forward through the
remainder of `t` to find a match, restarting the search position each
time.

Why it's not ideal: can degrade toward O(n·m) in naive implementations if
search positions aren't carefully tracked.

**Optimized — two pointers, single pass through both strings:** walk `i`
through `s` and `j` through `t` simultaneously. Advance `j` every step. Only
advance `i` when `s[i] == t[j]` — a match has been found for the current
character of `s`, so move on to looking for the next one. At the end, if
`i` has reached the end of `s`, every character was matched in order, so
`s` is a subsequence of `t`.

Why it works: a subsequence only needs characters to appear in the same
relative order, not contiguously — so greedily matching the earliest
possible occurrence of each character of `s` in `t` is always a safe
choice; matching later can never help and might miss room for the
remaining characters.

## Complexity

| | Brute force | Optimized (two pointers) |
|---|---|---|
| Time | O(n·m) worst case | O(m), m = length of `t` |
| Space | O(1) | O(1) |

## Key pattern

Two pointers advancing through two sequences in lockstep, with one
pointer only moving on a match — a lightweight alternative to full
edit-distance/DP string-matching when only subsequence membership (not
alignment or distance) is needed. Worth noting the DP tag here: this same
problem generalizes to DP when solved repeatedly against many different
`s` strings against a fixed `t`.
