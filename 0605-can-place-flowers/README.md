# [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

**Difficulty:** Easy
**Topics:** Array, Greedy

## Approach

**Brute force:** there isn't a meaningfully slower alternative here beyond
the single-pass greedy scan — the problem is inherently linear; the real
choice is whether the greedy "plant whenever possible" rule is provably
correct (it is).

**Approach used — greedy, single pass:** scan the flowerbed left to
right. At each empty plot (`0`), check whether both its left and right
neighbors are also empty (or off the edge of the array, treated as
empty). If so, plant a flower there immediately (`flowerbed[i] = 1`) and
increment the count. Stop early and return `true` the moment `count >= n`.

Why it works: planting as early as possible whenever it's legal is always
at least as good as waiting — delaying a plant can never create *more*
opportunities later, since every plot you skip is still available to the
next check regardless. So the greedy choice at each step never costs you
anything compared to a smarter global strategy.

## Complexity

| | Approach used (greedy) |
|---|---|
| Time | O(n) |
| Space | O(1) |

## Key pattern

Greedy left-to-right scan with a local "is it safe here?" check
(neighbors on both sides) — works because committing early never closes
off a better option later. Common in scheduling/placement problems framed
as 1D arrays.
