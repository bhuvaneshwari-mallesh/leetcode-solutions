# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**Difficulty:** Easy  
**Topics:** String, Stack, Bracket Sequences

## Approach

**Brute force:** Repeatedly searching for and removing adjacent valid bracket pairs (`()`, `[]`, `{}`) from the string until no more reductions can be made. This falls short because in the worst-case scenario (e.g., deeply nested or long mismatched strings), string modification or repeated scanning takes $O(n^2)$ or $O(n^3)$ time, easily timing out.

**Optimized:** We iterate through the string using a stack to keep track of expected closing brackets. When we encounter an opening bracket, we push its corresponding closing partner (or vice versa) onto the stack; when we hit a closing bracket, we pop from the stack and verify it matches the current character. If the stack is empty, the top doesn't match, or anything remains in the stack at the end, the string is invalid.

## Complexity

| Operation | Brute Force | Optimized |
| :--- | :--- | :--- |
| **Time** | $O(n^2)$ | $O(n)$ |
| **Space** | $O(n)$ | $O(n)$ |

## Key pattern

Bracket matching with a stack, which is the foundational technique for parsing nested structures, evaluating expressions, and syntax validation in compilers.
