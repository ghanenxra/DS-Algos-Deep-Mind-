'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def sumBT(self, root):
        #code here
        if root is None:
            return 0
            
        
        else:
            return self.sumBT(root.left)+self.sumBT(root.right) + (root.data)