# [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

**Difficulty:** Easy  
**Topics:** Stack, Design, Queue

## Approach

**Brute force:** We could use two queues to maintain the stack order, pushing to one queue and shifting elements back and forth during pops to keep the LIFO order. This makes operations lopsided and adds unnecessary data movement.

**Optimized:** We can implement a stack using a single queue by doing the heavy lifting during the `push` operation. Whenever a new element is pushed, we append it and then immediately rotate the queue by popping and re-appending all previous elements. This keeps the newly added element at the front of the queue, satisfying LIFO behavior so that `pop` and `top` become $O(1)$ operations.

## Complexity

| Operation | Brute force | Optimized |
| :--- | :--- | :--- |
| Time | $O(N)$ push / $O(1)$ pop | $O(N)$ push / $O(1)$ pop, top, empty |
| Space | $O(N)$ | $O(N)$ |

## Key pattern

This demonstrates the "Data Structure Adaptation" pattern, where one standard linear collection is re-engineered via clever repositioning upon insertion to mimic the interface of another. It commonly shows up in interview design questions and parser implementation problems.
