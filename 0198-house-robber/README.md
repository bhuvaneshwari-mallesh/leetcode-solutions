# [198. House Robber](https://leetcode.com/problems/house-robber/)

**Difficulty:** Medium  
**Topics:** Array, Dynamic Programming

## Approach

**Brute force:** We could generate all possible non-adjacent subsets of houses and find the one with the maximum sum. This requires exploring an exponential number of combinations, leading to an $O(2^n)$ time complexity which quickly TLEs.

**Optimized:** We can use dynamic programming by realizing that at any house $i$, we have two choices: either rob this house and add its loot to the max loot from two houses ago (`nums[i] + dp[i-2]`), or skip it and keep the max loot from the previous house (`dp[i-1]`). The state transition `dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])` builds the optimal substructure incrementally from left to right.

## Complexity

| Operation | Brute Force | Optimized |
| :--- | :--- | :--- |
| Time | $O(2^n)$ | $O(n)$ |
| Space | $O(n)$ | $O(n)$ |

## Key pattern

This demonstrates the 1D Dynamic Programming / Choice-based State Transition pattern, which shows up in problems where you make sequential choices with restrictions, such as Delete and Earn or House Robber II.
