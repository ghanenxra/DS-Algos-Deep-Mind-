class Solution:
    def floorSqrt(self, n):
        
        if n<2:
            return n
            
        left = 1
        right = n
        
        while left <= right:
            mid = (left+right)//2
            
            squared_no = mid * mid
            
            if squared_no == n:
                return mid
                
            elif squared_no < n:
                left  = mid+1
                
            elif squared_no > n:
                right = mid-1
        
        return right
        
        
        