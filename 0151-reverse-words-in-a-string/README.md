# [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

**Difficulty:** Medium
**Topics:** Two Pointers, String

## Approach

**Brute force:** manually scan character by character to find word
boundaries, building each word and a reversed list by hand.

Why it's not ideal: easy to get wrong with edge cases (leading/trailing
spaces, multiple spaces between words), and reinvents what string
splitting already does cleanly.

**Approach used — split, reverse the word list, rejoin:**

1. `s.trim().split("\\s+")` — trims leading/trailing whitespace and splits
   on any run of whitespace, so multiple spaces between words collapse
   into single separators and don't produce empty "words."
2. Walk the resulting word array back-to-front, copying into a new array
   in reversed order.
3. Join the reversed array back into a single string with single spaces.

Why it works: splitting on whitespace regex handles all the messy
whitespace edge cases in one step, so the only real work left is reversing
the order of a clean list of words — far simpler than reversing in place
character by character.

## Complexity

| | Approach used |
|---|---|
| Time | O(n) |
| Space | O(n) (word array + result) |

## Key pattern

Split → reverse the unit of interest (words, not characters) → rejoin —
useful whenever "reverse order" needs to apply at a coarser granularity
than individual characters.
