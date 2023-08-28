class MyStack:

    def __init__(self):
        self.deque = deque()
    def push(self, x: int) -> None:
        self.deque.appendleft(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        
        top = self.deque[0]
        self.deque.popleft()
        return top

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return len(self.deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()