class Solution:
    def isPowerOfEight(self, n):
        if n>0 and n&(n-1)==0 and n%7==1:
            return True
        return False