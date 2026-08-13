''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        #
            
        temp = head
        
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
            
        return head
        
        
        
        
        