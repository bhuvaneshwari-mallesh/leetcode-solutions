# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Difficulty:** Easy  
**Topics:** Linked List, Recursion

## Approach

**Brute force:** We could traverse the entire list and push all values into an array, then either rebuild a new linked list or overwrite the values in reverse order. This works and runs in $O(n)$ time, but it wastes $O(n)$ extra space to store the values when we should be able to reverse the pointers in place.

**Optimized:** Maintain two pointers—`prev` initialized to `None` and `curr` initialized to `head`—then iterate through the list while rewiring `curr.next` to point backward to `prev`. We cache `curr.next` in a temporary variable before breaking the link so we don't lose the rest of the list. Once `curr` runs off the end (`None`), `prev` is sitting on the new head of the reversed list.

## Complexity

| Operation | Brute force | Optimized |
| :--- | :--- | :--- |
| Time | $O(n)$ | $O(n)$ |
| Space | $O(n)$ | $O(1)$ |

## Key pattern

Pointer manipulation / In-place reversal, a fundamental linked list pattern that shows up whenever you need to restructure nodes without allocating auxiliary data structures.
