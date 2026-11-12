# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

**Difficulty:** Medium
**Topics:** Array, Hash Table, Union-Find

## Approach

**Brute force:** sort the array, then scan through counting the length of
each run of consecutive numbers.

Why it's not enough: sorting is O(n log n), and the problem explicitly
wants O(n) — the sorted-order dependency has to be removed entirely.

**Optimized — hash set + "only start counting at sequence starts":** put
every number into a set for O(1) lookup. Then, for each number, only begin
counting a sequence from it if `num - 1` is **not** in the set — meaning
it's the smallest number in its run, i.e. a true sequence start. From
there, walk forward (`num + 1`, `num + 2`, ...) counting how far the
consecutive run extends.

Why it works: the "only start at sequence starts" check is what keeps this
O(n) instead of O(n²) — without it, every number inside a long run would
redundantly re-walk the same sequence from scratch. With the check, each
number is only ever the start of its own run once, so every number across
the whole array is visited a total of O(1) times on average, even though
it looks like a nested loop.

## Complexity

| | Brute force (sort) | Optimized (hash set) |
|---|---|---|
| Time | O(n log n) | O(n) |
| Space | O(1) – O(n) (sort-dependent) | O(n) (the set) |

## Key pattern

Hash set + "only process true starting points" — turns what looks like
O(n²) work into O(n) by making sure each element only does real work once,
as the start of its own run.
