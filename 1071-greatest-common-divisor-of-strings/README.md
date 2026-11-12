# [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

**Difficulty:** Easy
**Topics:** Math, String, Euclidean Algorithm, Greatest Common Divisor

## Approach

**Brute force:** try every prefix length from the shorter string's length
down to 1, checking at each length whether that prefix, repeated, can
tile both `str1` and `str2` exactly.

Why it's not ideal: checking "does this prefix tile both strings" at every
candidate length redundantly re-verifies a lot of structure that a
single up-front check can rule out in one shot.

**Optimized — numeric GCD of the lengths, after a quick validity check:**

1. **Validity check:** if a common "divisor string" exists at all, then
   `str1 + str2` must equal `str2 + str1` (concatenating them in either
   order gives the same result) — this is both necessary and sufficient
   for a valid answer to exist. If it fails, return `""` immediately.
2. If it passes, the length of the answer is exactly
   `gcd(len(str1), len(str2))` — computed with the standard recursive
   Euclidean algorithm.
3. The answer itself is just `str1`'s prefix of that length.

Why it works: the string-GCD problem reduces directly to the numeric GCD
problem once the `str1+str2 == str2+str1` property is confirmed — a classic
example of recognizing that a string problem has an underlying math
structure (period/divisibility) rather than needing to be solved purely
with string manipulation.

## Complexity

| | Brute force | Optimized (concat check + numeric GCD) |
|---|---|---|
| Time | O(n + m) for the concat check, O(log(min(n,m))) for GCD | O(n + m) |
| Space | O(n + m) (string concatenation) | O(n + m) |

## Key pattern

Recognizing when a string problem is secretly a number-theory problem
(here, GCD) — the `s1+s2 == s2+s1` check is a reusable trick for detecting
whether two strings share a common "base" repeating unit.
