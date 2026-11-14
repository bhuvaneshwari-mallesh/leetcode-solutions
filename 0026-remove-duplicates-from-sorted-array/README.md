# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Difficulty:** Easy  
**Topics:** Array, Two Pointers

## Approach

**Brute force:** We could use a hash set or a secondary array to track unique elements, then copy them back into the original array. This falls short because it violates the $O(1)$ extra space constraint required by the problem.

**Optimized:** Since the array is already sorted, duplicates will always be adjacent to each other. We use a two-pointer approach where a slow pointer (`i` or `slow`) keeps track of the position of the last unique element, and a fast pointer scans ahead. Whenever the fast pointer encounters a new unique value, we advance the slow pointer and overwrite the next position with the new value.

## Complexity

| Operation | Brute Force | Optimized |
| :--- | :--- | :--- |
| Time | $O(N)$ | $O(N)$ |
| Space | $O(N)$ | $O(1)$ |

## Key pattern

This is a classic **Two Pointers (Fast and Slow)** pattern used for in-place array modifications. It shows up frequently in problems where you need to filter, partition, or remove elements from a sequence without allocating extra memory.
