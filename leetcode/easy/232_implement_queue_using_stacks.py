class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        """out が空のときだけ in から全部移す"""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
    
    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self._transfer()
        return self.out_stack.pop()
        

    def peek(self):
        self._transfer()
        return self.out_stack[-1]      # 取り出さずに見るだけ

    def empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
#Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
