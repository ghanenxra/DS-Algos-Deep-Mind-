class Solution:
    def countOnes(self, arr):
        i = 0
        j = len(arr)-1
        
        while i<=j:
            mid = (i+j)//2
            
            if arr[mid] == 1:
                i = mid + 1
                
            elif arr[mid] == 0:
                j = mid - 1
                
        return i
            
        