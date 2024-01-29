class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_queue = []
        

    def push(self, x: int) -> None:
        self.my_queue.append(x)
        

    def pop(self) -> int:
        return self.my_queue.pop(0)
        

    def peek(self) -> int:
        return self.my_queue[0]
        

    def empty(self) -> bool:
        return len(self.my_queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()