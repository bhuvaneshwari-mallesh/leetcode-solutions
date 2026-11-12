# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Difficulty:** Easy
**Topics:** Array, Dynamic Programming

## Approach

**Brute force:** check every pair of buy/sell days `(i, j)` with `j > i`,
compute `prices[j] - prices[i]`, and track the max.

Why it's not enough: O(n²) pairs.

**Optimized — track the minimum price seen so far:** walk the array once.
At each day, update `min_price` if the current price is a new low; then
check if selling today (`price - min_price`) beats the best profit found
so far.

- **Python solution:** exactly this — single pass, `min_price` and
  `best_profit` updated together.
- **Java solution:** a slightly different framing using two pointers `i`
  (potential buy day) and `j` (potential sell day) walking together — `i`
  jumps forward whenever a new low is found, otherwise the profit at `j`
  is checked against the running max. Same underlying idea, different
  bookkeeping.

Why it works: the best sell day for any given buy day only ever depends on
the lowest price seen *before* it — so tracking the running minimum as you
go is enough; there's no need to look back and recheck earlier days.

## Complexity

| | Brute force | Optimized |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |

## Key pattern

Running minimum (or maximum) tracked alongside a running best answer — a
single-pass pattern anywhere the question is "best difference against
something earlier in the sequence."
