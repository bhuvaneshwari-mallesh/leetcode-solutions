# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Dynamic Programming

## Approach

**Brute force:** check every possible subarray `(i, j)`, sum it, and track
the max.

Why it's not enough: O(n²) (or O(n³) with naive re-summing each time).

**Optimized — Kadane's algorithm:** walk the array once, keeping a running
`current_sum`. At each element, decide: is it better to extend the
existing subarray (`current_sum + num`), or start fresh from this element
alone (`num`)? Take whichever is larger. Track the best `current_sum` seen
at any point as `best_sum`.

Why it works: if `current_sum` ever drops below the value of the current
element itself, carrying that negative baggage forward can only hurt
future sums — so it's always at least as good to restart. This greedy,
local decision at each step turns out to always lead to the globally
optimal subarray, without needing to look back.

## Complexity

| | Brute force | Optimized (Kadane's) |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |

## Key pattern

Kadane's algorithm — "extend or restart" is a classic DP-flavored greedy
pattern for max/min subarray problems. Worth recognizing by name; it comes
up often enough to be its own pattern rather than being re-derived each
time.
