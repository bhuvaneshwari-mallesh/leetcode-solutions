# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

**Difficulty:** Medium
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

## Approach

**Brute force:** count frequencies, then for `k` rounds, scan the whole
frequency map to find and remove the current max each time.

Why it's not enough: O(n·k) in the worst case if the max is re-found from
scratch each round.

**Approach used — count, then sort by frequency:** build a frequency
`dict` for every number, then `sorted(count.items(), key=lambda pair:
pair[1], reverse=True)` sorts all (number, frequency) pairs by frequency
descending, and the first `k` pairs' numbers are the answer.

Why it works: sorting gives every number's rank by frequency in one shot,
so the top `k` are just the first `k` entries — simpler to write than the
bucket-sort or heap approaches, at the cost of doing more sorting work
than those optimal approaches need.

**Worth knowing — the topic tags point at faster options:** this problem
can be done in O(n) using **bucket sort** (bucket index = frequency, since
frequency is bounded by array length) or in O(n log k) using a **min-heap
of size k**. Both avoid sorting *all* n elements just to get the top k.
Not what's implemented here, but worth knowing since the tags specifically
call them out as the intended optimal approaches.

## Complexity

| | Brute force | Used (sort by frequency) | Bucket sort (not used, optimal) | Heap of size k (not used) |
|---|---|---|---|---|
| Time | O(n·k) | O(n log n) | O(n) | O(n log k) |
| Space | O(n) | O(n) | O(n) | O(k) |

## Key pattern

"Sort by frequency" is a clean, easy-to-write baseline for top-k problems;
bucket sort (when frequency is bounded) and a size-k heap are the two
standard upgrades when `n log n` isn't good enough.
