# [55. Jump Game](https://leetcode.com/problems/jump-game/)

**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming, Greedy

## Approach

**Brute force:** We could recursively explore every possible jump length from each index to see if we eventually reach the last index. This falls short with an $O(2^n)$ time complexity because of overlapping subproblems, hitting a Time Limit Exceeded on larger arrays.

**Optimized:** Instead of tracking every path, we can reframe the problem as maintaining a running maximum of the furthest reachable index. As we iterate through the array, if we ever encounter an index that exceeds our current `farthest` reach, we know we're stuck and return `false`. Otherwise, we greedily update our maximum reach and can exit early as soon as `farthest` reaches or passes the final index.

## Complexity

| Approach | Time | Space |
| :--- | :--- | :--- |
| Brute force | $O(2^n)$ | $O(n)$ |
| Greedy | $O(n)$ | $O(1)$ |

## Key pattern

This demonstrates the greedy interval/reachability pattern, which frequently appears in problems involving coverage, merging intervals, or determining if a destination can be reached with limited resources.
