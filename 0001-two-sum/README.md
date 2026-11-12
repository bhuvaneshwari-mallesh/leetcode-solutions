# [1. Two Sum](https://leetcode.com/problems/two-sum/)

**Difficulty:** Easy
**Topics:** Array, Hash Table

## Approach

**Brute force:** check every pair `(i, j)` and see if `nums[i] + nums[j] == target`.

```python
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
```

Why it's not enough: nested loop → O(n²).

**Optimized — hash map of complements:** walk the array once. At each index,
compute `complement = target - nums[i]`. If `complement` is already in the
map, its paired index plus the current index is the answer; otherwise store
`nums[i] -> i` and keep going.

Why it works: a hash map gives O(1) average lookup, so "have I seen the
number I need?" is answered instantly instead of by re-scanning. One pass
is enough because by the time you reach the second half of a valid pair,
the first half is already in the map.

## Complexity

| | Brute force | Optimized |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(n) (the hash map) |

## Key pattern

Complement lookup via hash map — "have I seen what I need to pair with
this?" shows up across a huge range of array/string problems whenever a
pairwise or target-sum condition is involved.
