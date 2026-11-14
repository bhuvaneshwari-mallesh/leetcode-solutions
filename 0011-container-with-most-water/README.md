# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Difficulty:** Medium  
**Topics:** Array, Two Pointers, Greedy

## Approach

**Brute force:** Check every possible pair of lines by nested looping through all indices $i$ and $j$ to calculate their enclosed area, tracking the maximum. This takes $O(n^2)$ time, which TLEs given the constraints.

**Optimized:** Start with pointers at both ends of the array and greedily shrink the window by moving the pointer pointing to the shorter line inward. Since the area is bounded by the shorter line, moving the taller line inward could only ever decrease the width without any hope of finding a taller bounding height, so we only discard the constraint-limiting side in search of a better container.

## Complexity

| Axis | Brute force | Optimized |
| :--- | :--- | :--- |
| Time | $O(n^2)$ | $O(n)$ |
| Space | $O(1)$ | $O(1)$ |

## Key pattern

This uses the Two Pointers technique converging from opposite ends, driven by a greedy choice to discard suboptimal states. It shows up frequently in array problems dealing with pairs, subarrays, or bounds (like 3Sum or Trapping Rain Water).
