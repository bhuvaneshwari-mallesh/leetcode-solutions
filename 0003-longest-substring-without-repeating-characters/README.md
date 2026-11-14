# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Difficulty:** Medium  
**Topics:** Hash Table, String, Sliding Window

## Approach

**Brute force:** Generate every possible substring and check each one for duplicate characters using a set. This takes $O(n^3)$ time (or $O(n^2)$ if you check characters on the fly), which instantly TLEs on larger inputs since we're redundantly re-checking overlapping substrings.

**Optimized:** Use a sliding window defined by a `left` and `right` pointer, alongside a set to track the characters currently in the window. As the `right` pointer expands, if we hit a duplicate character, we shrink the window from the `left` until the duplicate is evicted. This works because any time a conflict occurs at `right`, we only need to advance `left` just past the previous occurrence of that character to maintain a valid substring, tracking the maximum window size along the way.

## Complexity

| Approach | Time | Space |
| :--- | :--- | :--- |
| Brute force | $O(n^2)$ or $O(n^3)$ | $O(min(n, m))$ |
| Optimized (Sliding Window) | $O(n)$ | $O(min(n, m))$ |

*(Note: $n$ is the length of the string, and $m$ is the size of the charset)*

## Key pattern

This is the classic **Sliding Window** pattern, which is heavily used for problems involving contiguous subarrays or substrings where you need to dynamically expand and contract a range to satisfy a condition.
