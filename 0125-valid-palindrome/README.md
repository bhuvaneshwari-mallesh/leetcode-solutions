# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Difficulty:** Easy
**Topics:** Two Pointers, String

## Approach

**Brute force:** build a cleaned string (lowercase, alphanumeric only),
then compare it against its own reverse.

Why it's not ideal: building a reversed copy uses O(n) extra space beyond
the cleaned string itself, which is avoidable.

**Optimized — two pointers from both ends:**

- **Python solution:** builds the cleaned list first (`[ch.lower() for ch
  in s if ch.isalnum()]`), then walks `left`/`right` pointers inward,
  comparing as it goes — stops early the moment a mismatch is found.
- **Java solution:** skips building a cleaned copy at all — `left` and
  `right` pointers walk the *original* string directly, each one skipping
  past non-alphanumeric characters inline (`isLetterOrDigit`) before the
  comparison, so nothing extra is ever allocated.

Why it works: a palindrome check only needs to compare matching pairs from
the outside in — the moment one pair disagrees, the answer is already
known, so there's no need to fully construct or reverse anything.

## Complexity

| | Brute force (cleaned + reversed copy) | Python (cleaned list + two pointers) | Java (two pointers, no copy) |
|---|---|---|---|
| Time | O(n) | O(n) | O(n) |
| Space | O(n) | O(n) (cleaned list) | O(1) extra |

## Key pattern

Two pointers converging from both ends with inline filtering — avoids a
separate cleaning pass entirely when the language/implementation allows
skipping characters on the fly (as in the Java version here).
