# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

**Difficulty:** Easy
**Topics:** Hash Table, String, Sorting

## Approach

**Brute force:** sort both strings and compare them for equality.

Why it's not ideal: O(n log n) from sorting, when counting characters can
do it in linear time.

**Optimized — character counting:**

- **Java solution:** uses a fixed-size `int[26]` array (assumes lowercase
  English letters). Increment the count for each character of `s`,
  decrement for each character of `t`. If `s` and `t` are true anagrams,
  every slot ends up back at 0.
- **Python solution:** builds two separate `dict`s, counting characters of
  `s` and `t` independently, then compares the two dictionaries for
  equality.

Why it works: two strings are anagrams exactly when they contain the same
characters the same number of times — counting (rather than sorting)
captures that directly in one pass, and comparing counts is cheaper than
sorting and comparing character sequences.

## Complexity

| | Brute force (sort) | Java (fixed array, net counts) | Python (two dicts) |
|---|---|---|---|
| Time | O(n log n) | O(n) | O(n) |
| Space | O(1) (in-place sort) / O(n) | O(1) — fixed 26-slot array | O(n) — two dicts |

## Key pattern

Character frequency counting instead of sorting for anagram-style
comparisons — the Java version's "increment for one string, decrement for
the other, check all-zero" is a nice space-saving variant worth
remembering over keeping two separate counters.
