'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        arr1 = []
        temp = head
        while temp:
            arr1.append(temp.data)
            temp = temp.next
        return arr1