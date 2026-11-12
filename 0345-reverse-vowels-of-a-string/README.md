# [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

**Difficulty:** Easy
**Topics:** Two Pointers, String

## Approach

**Brute force:** scan the string to collect all vowels and their
positions into a separate list, reverse that list, then build a new
string placing the reversed vowels back at their original positions.

Why it's not ideal: uses extra structures to track positions separately,
when two pointers can do the swap directly in place.

**Optimized — two pointers from both ends:** convert the string to a
character array (needed since strings are immutable). Walk `i` from the
start and `j` from the end inward; skip past any non-vowel characters on
either side; when both `i` and `j` land on vowels, swap them; repeat until
the pointers meet.

Why it works: only vowels need to move, and only relative to each other —
consonants stay exactly where they are. Two pointers converging from both
ends naturally pair up the first and last vowel, then the second and
second-to-last, and so on, which is exactly the "reversed" order required
— no separate position tracking needed.

## Complexity

| | Brute force (separate vowel list) | Optimized (two pointers, in place) |
|---|---|---|
| Time | O(n) | O(n) |
| Space | O(n) (vowel list + new string) | O(n) (char array, required since strings are immutable) |

## Key pattern

Two pointers converging inward, skipping irrelevant elements on both
sides — same shape as Valid Palindrome, applied here to selectively swap
rather than just compare.
