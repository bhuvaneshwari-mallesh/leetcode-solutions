# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Difficulty:** Medium
**Topics:** Array, Binary Search, Sliding Window, Prefix Sum

## Approach

**Brute force:** check every subarray, sum it, and track the shortest one
whose sum is `>= target`.

Why it's not enough: O(n²) (or O(n³) with naive re-summing per subarray).

**Optimized — variable-size sliding window:** expand a window by moving
`right` forward, adding each element to a running `sum`. The moment
`sum >= target`, the window is valid — record its length, then shrink from
`left`, subtracting as you go, for as long as it stays valid, to find the
*smallest* valid window ending near this point before continuing to
expand `right` again.

Why it works: since all numbers are positive, growing the window can only
increase the sum, and shrinking it can only decrease it — so the window
boundary behaves predictably in both directions, which is exactly what
lets two pointers replace a nested loop. Every element is added once and
removed at most once across the whole scan, keeping it linear.

## Complexity

| | Brute force | Optimized (sliding window) |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |

## Key pattern

Variable-size sliding window for "shortest/longest subarray meeting a sum
condition" — relies on all values being positive so the window shrinks and
grows monotonically; same family as the sliding window used in Longest
Substring Without Repeating Characters.
