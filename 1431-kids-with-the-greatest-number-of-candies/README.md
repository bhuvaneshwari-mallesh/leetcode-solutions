# [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

**Difficulty:** Easy
**Topics:** Array

## Approach

This problem doesn't really have a meaningfully different brute force —
finding the max requires at least one pass, and checking each kid requires
at least a second pass (or a single combined pass if the max were known in
advance, which it isn't until the array is scanned). The solution here is
already the natural linear approach, just split into two clear steps.

**Approach used — two linear passes:**

1. First pass: find `max`, the highest candy count in the array.
2. Second pass: for each kid, check whether `candies[i] + extraCandies >=
   max` — if so, they could have the most candies after receiving the
   extras; record `true`/`false` accordingly.

Why it works: the "greatest number of candies" bar is fixed once the
current max is known, so each kid's eligibility only needs comparing
against that one fixed number — no need to compare kids against each
other directly.

## Complexity

| | Approach used |
|---|---|
| Time | O(n) — two linear passes |
| Space | O(n) — the result list (O(1) extra beyond that) |

## Key pattern

Find-the-bar-first, then-check-everyone-against-it — a simple two-pass
shape that shows up whenever a condition depends on a single global
max/min that must be known before anything else can be evaluated.
