class Solution:
    def binarySearch(self, arr, k):
        
        initial = 0
        final = len(arr)-1
        
        while initial <= final:
            mid = (initial + final)//2
            
            if arr[mid] == k:
                return True
                
            elif arr[mid] < k:
                initial = mid + 1

            
            elif arr[mid] > k:
                final = mid - 1
                
                
        return False
        
        