"""
Approaches: Queue using 2 Stacks

        1. Push O(1) Pop O(N): 
            push ele in 1st stack than when it comes to pop.....Insert all elements to 2nd stack till n-1 than return last ele
            
        2. Push O(N) Pop O(1): 
            For pushing shift all 1st stacks existing ele's to 2nd stack than append in 1st stack now again shift to 2nd to 1st
            
        3. Push And Pop in O(1) Amortized:
            a. Take 2 stacks input and output
            b. push in input stack
            c. if Peek is called and output stack is empty than shift whole input --> output
                return output[-1]
                
            d. if pop is called pop from output stack if not empty else shift input --> output
                than pop from out
                
        LeetCode 232: https://leetcode.com/problems/implement-queue-using-stacks/
        YT: https://www.youtube.com/watch?v=3Et9MrMc02A
"""

class MyQueue:

    def __init__(self):
        self.inp = []
        self.out = []
        

    def push(self, x: int) -> None:
        self.inp.append(x)
        

    def pop(self) -> int:
        if self.out: return self.out.pop()
        else:
            while self.inp: 
                self.out.append(self.inp.pop())
            return self.out.pop()

    def peek(self) -> int:
        if self.out: return self.out[-1]
        else:
            while self.inp:
                self.out.append(self.inp.pop())
            return self.out[-1]
        

    def empty(self) -> bool:
        if not self.inp and not self.out: return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
