# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Difficulty:** Easy
**Topics:** Array, Two Pointers

## Approach

**Brute force:** use a set or a separate list to collect unique values,
then copy them back into `nums`.

Why it's not ideal: uses O(n) extra space, when the sorted order means
duplicates are already sitting next to each other.

**Optimized — two pointers, in place:** since the array is sorted,
duplicates are always adjacent. Keep a slow pointer `i` marking the last
confirmed-unique position, and a fast pointer `j` scanning ahead. Whenever
`nums[j] != nums[i]`, it's a genuinely new value — advance `i` and copy
`nums[j]` into that spot.

Why it works: because the array is sorted, "is this different from the
last unique value I kept?" is enough to detect every duplicate — no need
for a set. `i + 1` at the end is the count of unique elements, and the
first `i + 1` slots of `nums` hold them in order.

## Complexity

| | Brute force (with extra structure) | Optimized (two pointers) |
|---|---|---|
| Time | O(n) | O(n) |
| Space | O(n) | O(1) |

## Key pattern

Slow/fast pointer in-place compaction — overwrite the array as you go
using a "write pointer" that only advances when something worth keeping is
found. Reusable for in-place filtering/dedup problems generally.
