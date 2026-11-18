# [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Stack, Monotonic Stack

## Approach

**Brute force:** For each element in `nums1`, find its position in `nums2` and scan to the right until a larger element is found. This takes $O(N \times M)$ time where $N$ and $M$ are the lengths of the two arrays, which is inefficient since we end up repeatedly scanning the same subsegments of `nums2`.

**Optimized:** We can precompute the next greater element for every number in `nums2` in a single pass using a monotonic decreasing stack. As we iterate through `nums2`, any time we find a number larger than the element at the top of our stack, we've found the "next greater" for that stack element and can record it in a hash map. Once `nums2` is processed, we simply look up the answers for `nums1` in $O(1)$ time each.

## Complexity

| | Brute Force | Optimized |
|---|---|---|
| **Time** | $O(N \times M)$ | $O(N + M)$ |
| **Space** | $O(1)$ | $O(M)$ |

## Key pattern

Monotonic stack. This pattern is essential for problems asking to find the "next greater" or "previous smaller" element in an array, and frequently appears in histogram and sliding window maximum problems.
