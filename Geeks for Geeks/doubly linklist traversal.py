''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        
        if head is None:
            return [[],[]]
            
        arr1 = []
        arr2 = []
        
        temp = head
        
        while temp:
            arr1.append(temp.data)
            tail = temp
            temp = temp.next
            
        temp = tail
        
        while temp:
            arr2.append(temp.data)
            temp=temp.prev
            
        return [arr1 , arr2]
        
        
        