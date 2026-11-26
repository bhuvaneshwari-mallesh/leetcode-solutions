# [72. Edit Distance](https://leetcode.com/problems/edit-distance/)

**Difficulty:** Medium  
**Topics:** String, Dynamic Programming

## Approach

**Brute force:** Trying every possible sequence of insertions, deletions, and replacements using recursion would explore an exponential search tree of choices at every character pair. This results in redundant subproblems and blows up exponentially, leading to a Time Limit Exceeded error.

**Optimized:** We use a 2D dynamic programming table where `dp[i][j]` represents the minimum operations to convert the first $i$ characters of `word1` into the first $j$ characters of `word2`. If the current characters match, we inherit the cost from the diagonal subproblem (`dp[i-1][j-1]`). If they don't, we take the minimum cost among the three possible operations—replace, delete, or insert—plus one for the current operation.

## Complexity

| Operation | Brute Force | Optimized |
| :--- | :--- | :--- |
| Time | $O(3^{\max(m, n)})$ | $O(m \times n)$ |
| Space | $O(m + n)$ (recursion stack) | $O(m \times n)$ |

## Key pattern

This demonstrates the classical 2D string Dynamic Programming pattern, where subproblems depend on adjacent prefixes (left, top, and diagonal). It frequently appears in sequence alignment and string transformation problems like Longest Common Subsequence or Interleaving String.
