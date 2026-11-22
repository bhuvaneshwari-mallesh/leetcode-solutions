# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

**Difficulty:** Easy  
**Topics:** Math, Dynamic Programming, Memoization

## Approach

**Brute force:** Recursively branching at every step by taking either 1 or 2 steps until reaching $n$. This essentially computes the same subproblems repeatedly, resulting in an exponential $O(2^n)$ time complexity that easily TLEs for larger inputs.

**Optimized:** Recognizing that the number of ways to reach step $n$ is simply the sum of the ways to reach step $n-1$ and step $n-2$, which maps directly to the Fibonacci sequence. We build an array from the bottom up—base cases at 0 and 1—where each entry stores the number of ways to reach that particular step.

## Complexity

| | Brute Force | Optimized |
| :--- | :--- | :--- |
| Time | $O(2^n)$ | $O(n)$ |
| Space | $O(n)$ | $O(n)$ |

## Key pattern

Bottom-up Dynamic Programming (Tabulation), which replaces redundant recursive calls with iterative state-building. This pattern is foundational for counting and optimization problems where solutions depend strictly on overlapping subproblems.
