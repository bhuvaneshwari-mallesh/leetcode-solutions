# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search

## Approach

**Brute force:** same as the original Two Sum — check every pair, O(n²).

Why it's not ideal here: the array being **sorted** is a huge hint that's
being wasted — a hash-map approach (O(n) time, O(n) space) also works, but
the sortedness enables something even leaner.

**Optimized — two pointers from both ends:** start `left` at index 0,
`right` at the last index. At each step:
- If `numbers[left] + numbers[right] == target` → found it, return
  (1-indexed, per the problem).
- If the sum is too small, move `left` right (need a bigger number).
- If the sum is too big, move `right` left (need a smaller number).

Why it works: because the array is sorted, moving `left` forward can only
increase the sum, and moving `right` backward can only decrease it. That
means each comparison safely eliminates one end as impossible — no pair
is ever skipped, and no extra space is needed to remember what's been
seen, unlike the hash-map approach.

## Complexity

| | Brute force | Hash map (works, unused here) | Optimized (two pointers) |
|---|---|---|---|
| Time | O(n²) | O(n) | O(n) |
| Space | O(1) | O(n) | O(1) |

## Key pattern

Two pointers on a **sorted** array to find a target pair — strictly better
than the hash-map version of Two Sum whenever sortedness is available,
since it drops the space cost to O(1).
