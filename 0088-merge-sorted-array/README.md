# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

**Difficulty:** Easy
**Topics:** Array, Two Pointers, Sorting

## Approach

**Brute force:** copy `nums2`'s elements into the tail of `nums1`, then
sort the whole thing.

Why it's not ideal: sorting is O((m+n) log(m+n)) when both arrays are
already individually sorted — that structure is being thrown away.

**Optimized — merge from the back, in place:** since `nums1` has exactly
`m + n` slots (the extra `n` are just padding), fill it from the **end**
backward instead of the front. Keep three pointers: `i` at the last real
element of `nums1`, `j` at the last element of `nums2`, `k` at the last
slot overall. Repeatedly place the larger of `nums1[i]` / `nums2[j]` at
`nums1[k]`, moving the relevant pointers inward.

Why it works: filling from the back means you're always writing into
slots that have already been read (or are still padding), so nothing gets
overwritten before it's used — unlike merging from the front, which would
require a separate buffer to avoid clobbering `nums1`'s own un-read
elements.

## Complexity

| | Brute force (copy + sort) | Optimized (merge from back) |
|---|---|---|
| Time | O((m+n) log(m+n)) | O(m + n) |
| Space | O(1) (sort in place) / O(log(m+n)) (typical sort call stack) | O(1) |

## Key pattern

Merging two sorted sequences from the back when writing in place — avoids
the overwrite problem that merging from the front would create, and is
the same idea behind the merge step of merge sort, adapted for in-place
constraints.
