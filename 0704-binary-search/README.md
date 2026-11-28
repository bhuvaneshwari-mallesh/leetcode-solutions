# [704. Binary Search](https://leetcode.com/problems/binary-search/)

**Difficulty:** Easy  
**Topics:** Array, Binary Search

## Approach

**Brute force:** Iterate through the entire array linearly and check every element until the target is found. This takes $O(N)$ time, which ignores the fact that the input array is already sorted.

**Optimized:** Use binary search by maintaining a `low` and `high` pointer that bracket our search space. By checking the middle element (`mid`) and halving the search space on each iteration (moving `low` up or `high` down depending on whether `nums[mid]` is smaller or larger than the target), we can zero in on the target logarithmically.

## Complexity

| Operation | Brute force | Optimized |
| :--- | :--- | :--- |
| Time | $O(N)$ | $O(\log N)$ |
| Space | $O(1)$ | $O(1)$ |

## Key pattern

Binary search, which demonstrates the "divide and conquer" or decrease-and-conquer technique on sorted data. This pattern shows up in various range-finding problems, finding boundaries in rotated sorted arrays, and monotonic search spaces.
