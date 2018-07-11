class MinStack:
    pointer = None
    class Node:        
        def __init__(self, val, min_v, next = None):
            self.val = val            
            self.min_v = min_v
            self.next = next               

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.pointer == None:
            self.pointer = self.Node(x, x)
        else:
            self.pointer = self.Node(x, min(x, self.pointer.min_v), self.pointer)
    def pop(self):
        """
        :rtype: void
        """
        if self.pointer != None:
            self.pointer = self.pointer.next      

    def top(self):
        """
        :rtype: int
        """
        if self.pointer != None:
            return self.pointer.val

    def getMin(self):
        """
        :rtype: int
        """
        if self.pointer != None:
            return self.pointer.min_v


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()