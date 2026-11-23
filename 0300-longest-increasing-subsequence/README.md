# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

**Difficulty:** Medium  
**Topics:** Array, Binary Search, Dynamic Programming, Longest Increasing Subsequence

## Approach

**Brute force:** Generate all possible subsequences, check each one to see if it's strictly increasing, and track the maximum length. This takes exponential time $O(2^n)$, which instantly times out for larger arrays since we're recomputing overlapping subproblems.

**Optimized:** Build up the answer dynamically by using an array `dp` where `dp[i]` stores the length of the longest increasing subsequence ending at index `i`. For each element, we look back at all previous elements; if a previous element is smaller, we can extend its subsequence by one. Taking the maximum value in `dp` at the end gives the overall longest increasing subsequence.

## Complexity

| Operation | Brute Force | Optimized |
| :--- | :--- | :--- |
| Time | $O(2^n)$ | $O(n^2)$ |
| Space | $O(n)$ | $O(n)$ |

## Key pattern

This demonstrates classical Dynamic Programming with state transition based on preceding subproblems, a pattern that shows up in sequence-based optimization problems like Edit Distance and Maximum Subarray.
