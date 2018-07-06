# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        priorityQ = []
        counter = 0
        for node in lists:
            if node:                
                heapq.heappush( priorityQ, (node.val, counter, node))
                counter += 1
        while priorityQ:
            val, _ , node = heapq.heappop(priorityQ)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:                
                heapq.heappush( priorityQ, (node.val, counter, node))
                counter += 1
        return head.next
                