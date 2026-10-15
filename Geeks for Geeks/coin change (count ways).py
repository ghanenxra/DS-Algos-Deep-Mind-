class Solution:
    def count(self, coins: list[int], sum: int) -> int:
        n=len(coins)
        dp=[[0]* (sum+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1

        for i in range(1,n+1):
            c=coins[i-1]
            for s in range(1, sum+1):
                dp[i][s]=dp[i-1][s]
                if s>=c:
                    dp[i][s]+=dp[i][s-c]
        return dp[n][sum]
        