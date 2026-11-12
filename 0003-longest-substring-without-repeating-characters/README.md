# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Difficulty:** Medium
**Topics:** Hash Table, String, Sliding Window

## Approach

**Brute force:** for every possible substring, check whether all its
characters are unique, and track the longest one that qualifies.

Why it's not enough: generating every substring is O(n²), and checking
each one for uniqueness adds another O(n) — O(n³) total (or O(n²) with a
smarter uniqueness check). Way too slow for large strings.

**Optimized — sliding window with a set:** keep a window `[left, right]`
that always holds unique characters, using a `HashSet` to track what's
currently inside it.

- Expand `right` one character at a time.
- If the new character is already in the set (a repeat *inside the current
  window*), shrink from `left`, removing characters, until the duplicate is
  gone.
- Track `right - left + 1` as a candidate for the longest length at every
  step.

Why it works: the window only ever grows or shrinks, each character is
added and removed from the set at most once across the whole scan — so
total work stays linear even though it looks like nested loops.

## Complexity

| | Brute force | Optimized |
|---|---|---|
| Time | O(n²) – O(n³) | O(n) |
| Space | O(min(n, charset size)) | O(min(n, charset size)) (the set) |

## Key pattern

Variable-size sliding window — grow the right edge to explore, shrink the
left edge to restore a broken invariant (here: "all characters unique").
Same shape reappears in minimum-size-subarray-sum style problems.
