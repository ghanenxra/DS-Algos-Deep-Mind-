cache = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n in cache:
            return cache[n]
        cache[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return cache[n]



        





        # if n <= 2:
        #     return n
        
        # prev2, prev1 = 1, 2
        
        # for _ in range(3, n + 1):
        #     curr = prev1 + prev2
        #     prev2 = prev1
        #     prev1 = curr
        
        # return prev1
