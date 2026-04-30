

Queue Practice Problems
A collection of common algorithmic challenges focused on the implementation and manipulation of Queue data structures using Python.

Problems Solved
1. Queue Implementation using Two Stacks
Objective: Implement a FIFO queue using two LIFO stacks.

Enqueue: O(1) - Elements are pushed directly onto an "in-stack."

Dequeue: Amortized O(1) - Elements are transferred to an "out-stack" only when needed, reversing their order to maintain FIFO behavior.

2. Queue Reversal
Objective: Reverse the order of elements in a queue using only a stack as auxiliary storage.

Logic: By dequeuing elements into a stack and then popping them back into the queue, the First-In-First-Out order is inverted into Last-In-First-Out.

3. Binary Number Generator
Objective: Generate the first N binary numbers using a queue.

Logic: Uses a Breadth-First Search (BFS) approach. Starting with "1", the algorithm dequeues a prefix and enqueues two new variations by appending "0" and "1" respectively.
