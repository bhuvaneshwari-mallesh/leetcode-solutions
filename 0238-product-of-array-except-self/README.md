# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

**Difficulty:** Medium
**Topics:** Array, Prefix Sum

## Approach

**Brute force:** for each index `i`, loop through the whole array again and
multiply every element except `nums[i]`.

```python
for i in range(n):
    product = 1
    for j in range(n):
        if j != i:
            product *= nums[j]
    answer.append(product)
```

Why it's not enough: nested loop → O(n²), too slow once `n` gets large.

The obvious shortcut — multiply everything once into `total`, then
`answer[i] = total / nums[i]` — is O(n) but breaks on a `0` in the array
(division by zero), and the problem disallows division anyway. So the real
ask is: get the effect of division without dividing.

**Optimized — prefix × suffix products:** `answer[i]` is just (product of
everything left of `i`) × (product of everything right of `i`). Precompute
both directions instead of recomputing from scratch per index.

- **Java solution:** one pass left→right fills `answer[i]` with the running
  prefix product (computed *before* folding in `nums[i]`, which is what
  keeps index `i` excluded); a second pass right→left multiplies in a
  running suffix product on top, in place.
- **Python solution:** same idea, built with two explicit arrays —
  `left_products[i]` and `right_products[i]` — then combined as
  `answer[i] = left_products[i] * right_products[i]`. More readable as a
  first pass at the pattern, at the cost of extra space the Java version
  avoids by writing into `answer` in place.

Why it works: no division, no nested loop — two linear passes.

## Complexity

| | Brute force | Optimized (Java, in-place) | Optimized (Python, two arrays) |
|---|---|---|---|
| Time | O(n²) | O(n) | O(n) |
| Space | O(1) extra | O(1) extra (output doesn't count) | O(n) extra (left + right arrays) |

## Key pattern

Prefix/suffix accumulation — same family of trick as trapping rain water or
running max/min from both directions. Worth remembering as its own reusable
pattern, not a one-off for this problem.
