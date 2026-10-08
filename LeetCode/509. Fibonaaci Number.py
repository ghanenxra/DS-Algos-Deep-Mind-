class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        first_ele = self.fib(n-1)
        second_ele = self.fib(n-2)

        return first_ele + second_ele

        # return n if n<=1 else self.fib(n-1)+self.fib(n-2) 
        """ Also did this one in single line """

        dp=[0]*(n+1) 
        if n<=1:
            return n
        dp[1]=1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
