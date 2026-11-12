# [169. Majority Element](https://leetcode.com/problems/majority-element/)

**Difficulty:** Easy
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm

## Approach

**Brute force:** for each number, count how many times it appears across
the whole array, and check if the count exceeds `n/2`.

Why it's not ideal: O(n²) if counting is redone from scratch per element.

**Approach used — hash map counting:** walk the array once, keeping a
running count of each number in a `HashMap`. The moment any number's count
exceeds `n/2`, it's guaranteed to be the majority element (the problem
guarantees one always exists) — return immediately.

Why it works: a majority element appears more than `n/2` times by
definition, so a single pass with a running tally is guaranteed to cross
that threshold at some point for the right element — no need to finish
counting every number fully before checking.

**Worth knowing — Boyer–Moore Voting Algorithm:** the topic tags call this
out specifically because there's an even leaner O(1)-space approach: keep
a `candidate` and a `count`. Increment `count` when you see `candidate`
again, decrement otherwise; swap to a new `candidate` whenever `count`
hits 0. The surviving candidate is the majority element. Not what's
implemented here, but worth knowing as the canonical optimal solution for
this exact problem.

## Complexity

| | Brute force | Hash map (used) | Boyer–Moore (not used, optimal) |
|---|---|---|---|
| Time | O(n²) | O(n) | O(n) |
| Space | O(1) | O(n) | O(1) |

## Key pattern

Hash map counting is the reliable O(n)/O(n) default for "find the element
that crosses a frequency threshold" — Boyer–Moore is the specialized
O(n)/O(1) upgrade specifically for the "more than n/2" majority case.
