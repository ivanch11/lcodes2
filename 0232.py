class MyQueue:
    
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.Front = None
        print ("init: ", len(self.stack1))

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop())      
        else:
            self.stack1.append(x)
            self.Front = x

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        if len(self.stack1) >= 1:
            k = self.stack1.pop()
            if len(self.stack1) > 0:
                self.Front = self.stack1.pop()
                self.stack1.append(self.Front)
            return k
        return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.Front
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        print (self.stack1)
        print (not self.stack1)
        print (len(self.stack1))
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()