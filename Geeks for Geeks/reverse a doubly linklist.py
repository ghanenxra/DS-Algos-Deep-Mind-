""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        
        temp = head
        
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            head = temp
            temp = temp.prev
            
        return head
        
        
        
        # tail = None
        
        # while temp.next:
        #     tail = temp
        #     temp = temp.next
        
        # return tail.prev