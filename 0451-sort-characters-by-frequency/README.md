# [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

**Difficulty:** Medium
**Topics:** Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting

## Approach

**Brute force:** repeatedly scan the frequency map to find and remove the
current most-frequent character, appending it to the result each round.

Why it's not enough: O(n·k) where k = number of distinct characters, if
the max is re-found from scratch each round.

**Approach used — count, then sort by frequency, then rebuild:**

1. Count every character's frequency into a `dict`.
2. Sort the (character, frequency) pairs by frequency, descending.
3. Rebuild the result string by repeating each character `freq` times, in
   that sorted order.

Why it works: once frequencies are sorted descending, writing each
character out `freq` times in that order directly produces a string where
higher-frequency characters appear in contiguous blocks before
lower-frequency ones — exactly what the problem asks for.

**Worth knowing:** same tradeoff as Top K Frequent Elements — **bucket
sort** (bucket index = frequency count, since it's bounded by string
length) would get this down to O(n) instead of paying the O(n log n) sort
cost. Not what's implemented here, but the natural upgrade given the
tags.

## Complexity

| | Brute force | Used (sort by frequency) | Bucket sort (not used, optimal) |
|---|---|---|---|
| Time | O(n·k) | O(n log n) | O(n) |
| Space | O(n) | O(n) | O(n) |

## Key pattern

Same "count → sort by frequency" shape as Top K Frequent Elements — worth
recognizing these two as the same underlying pattern applied to slightly
different outputs (a list of top elements vs. a rebuilt string).
