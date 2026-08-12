#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        if head is None:
            return True
            
        temp = head
        
        slow_temp = temp
        fast_temp = temp.next
        
        while fast_temp and fast_temp.next:
            slow_temp = slow_temp.next
            fast_temp = fast_temp.next.next
            
            if slow_temp == fast_temp:
                return True
                
        return False
        















        
        # # while temp!=None:
        # #     temp = temp.next
        # #     return False
        # # return True
        # while temp.next==head:
        #     temp = temp.next
        #     if temp==head:
        #         return True
        #     else:
        #          return False
        
              
        #     # elif temp != head:
        #     #     return False
        #     # break
        