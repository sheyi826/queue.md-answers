#1)Implement a Queue class using two stacks. Enqueue should be O(1); dequeue amortised O(1).
class MyQueue:
    def __init__(self):
        # Stack to handle incoming elements
        self.stack_in = []
        # Stack to handle outgoing elements
        self.stack_out = []

    def enqueue(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Time Complexity: O(1)
        """
        self.stack_in.append(x)

    def dequeue(self) -> int:
        """
        Removes the element from in front of queue and returns it.
        Time Complexity: Amortized O(1)
        """
        self._move_in_to_out()
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._move_in_to_out()
        if not self.stack_out:
            raise IndexError("peek from empty queue")
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out

    def _move_in_to_out(self) -> None:
        """
        Helper method to transfer elements when stack_out is empty.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

#2) Write a function that reverses the order of elements in a queue using only a stack as auxiliary storage.
from collections import deque

def reverse_queue(q):
    stack = []

    # Step 1: Dequeue everything and push to stack
    # This reverses the order because the first item in 
    # becomes the bottom item of the stack.
    while q:
        stack.append(q.popleft())

    # Step 2: Pop from stack and enqueue back
    # The last item pushed (the original tail) is now
    # the first item popped.
    while stack:
        q.append(stack.pop())
    
    return q

# Example Usage:
my_queue = deque([1, 2, 3, 4, 5])
print(f"Original: {list(my_queue)}")

reverse_queue(my_queue)
print(f"Reversed: {list(my_queue)}")  


#Given a queue, write a function to generate the first N binary numbers (1, 10, 11, 100...) using only a queue.
from collections import deque

def generate_binary_numbers(n):
    if n <= 0:
        return []

    # Initialize the queue with the first binary number
    q = deque()
    q.append("1")
    
    result = []

    for _ in range(n):
        # 1. Get the next binary number from the front
        current = q.popleft()
        result.append(current)
        
        # 2. Derive the next two numbers in the sequence
        # If current is "1", we generate "10" and "11"
        # If current is "10", we generate "100" and "101"
        q.append(current + "0")
        q.append(current + "1")

    return result

# Example Output for N = 6
# 1 -> 10, 11 -> 100, 101, 110, 111...
print(generate_binary_numbers(6))
# Output: ['1', '10', '11', '100', '101', '110']