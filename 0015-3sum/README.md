# [15. 3Sum](https://leetcode.com/problems/3sum/)

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Sorting

## Approach

**Brute force:** Check every possible triplet using three nested loops, which takes $O(n^3)$ time. Sorting the triplets to filter out duplicates doesn't save it from TLE given the input constraints.

**Optimized:** Sort the array first so we can use a fixed pointer combined with a two-pointer scan for the remaining two numbers. By sorting, if our current sum is too small we advance the left pointer, and if it's too large we decrement the right pointer. We also skip duplicate values for both the fixed number and the two pointers to ensure all returned triplets are unique without needing a set.

## Complexity

| Operation | Brute Force | Optimized |
| :--- | :--- | :--- |
| **Time** | $O(n^3)$ | $O(n^2)$ |
| **Space** | $O(1)$ or $O(n)$ | $O(1)$ |

## Key pattern

Sorting combined with Two Pointers to reduce higher-dimensional search spaces, a technique that frequently appears in problems requiring combination sums or pairs.
