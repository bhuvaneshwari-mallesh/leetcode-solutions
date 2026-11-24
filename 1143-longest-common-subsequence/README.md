# [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

**Difficulty:** Medium  
**Topics:** String, Dynamic Programming, Longest Common Subsequence

## Approach

**Brute force:** Generate all possible subsequences of `text1` and check if each one is a subsequence of `text2`, keeping track of the max length. Because the number of subsequences grows exponentially with the length of the strings ($2^n$), this approach takes $O(2^m \cdot n)$ time and times out immediately on moderate inputs.

**Optimized:** Build up the solution using a 2D dynamic programming table where `dp[i][j]` represents the length of the longest common subsequence of `text1[:i]` and `text2[:j]`. When characters match, we extend the best subsequence from
