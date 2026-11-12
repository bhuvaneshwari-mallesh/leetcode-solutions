# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

**Difficulty:** Medium
**Topics:** Array, Hash Table, Prefix Sum

## Approach

**Brute force:** check every subarray `(i, j)`, sum it, and count how many
sums equal `k`.

Why it's not enough: O(n²) (or O(n³) with naive re-summing per subarray).

**Optimized — prefix sum + hash map:** keep a running prefix sum
(`currSum`) as you scan left to right, and a hash map of *how many times
each prefix sum value has occurred so far*. For the current prefix sum, the
number of valid subarrays ending here that sum to `k` equals the number of
times `currSum - k` has been seen before — because if some earlier prefix
sum was `currSum - k`, the elements between that point and here must sum
to exactly `k`. After checking, record the current `currSum` in the map
(incrementing its count).

Why it works: any subarray sum can be expressed as a difference of two
prefix sums, `prefixSum[j] - prefixSum[i] = k`. Rearranged, that's
`prefixSum[i] = prefixSum[j] - k` — so instead of checking every possible
`i` for every `j`, a hash map turns "how many earlier prefix sums equal
`currSum - k`?" into an O(1) lookup.

## Complexity

| | Brute force | Optimized (prefix sum + hash map) |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(n) |

## Key pattern

Prefix sum + hash map of prefix-sum frequencies — the standard way to
count subarrays matching a sum condition in one pass, especially useful
since it works even with negative numbers (unlike a sliding window, which
needs all-positive values to behave monotonically).
