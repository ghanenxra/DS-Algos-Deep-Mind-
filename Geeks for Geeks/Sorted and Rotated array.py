class Solution:
    def findMin(self, arr):
        
        i = 0
        j = len(arr)-1
        
        while i < j:
            mid = (i+j)//2
            
            if arr[mid] > arr[j]:
                i = mid + 1 
                
            elif arr[mid] <= arr[j]:
                j = mid
                
        return arr[i]
        