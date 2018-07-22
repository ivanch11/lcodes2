# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []

        while l1:
            stack1 += [l1.val]
            l1 = l1.next
        while l2:
            stack2 += [l2.val]
            l2 = l2.next
        ansList = ListNode(0)
        sum = 0
        print ("stack1: ", stack1)
        print ("stack2: ", stack2)
        print ("ansList: ", ansList)
        while stack1 or stack2:
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            ansList.val = sum % 10
            sum //= 10
            temp = ListNode(sum)
            temp.next = ansList
            ansList = temp      
            
        return ansList if ansList.val != 0 else ansList.next