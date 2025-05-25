def uniquePaths(m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for y in range(1,n):
            for x in range(1,m):
                dp[y][x]=dp[y-1][x]+dp[y][x-1]

        return dp[n-1][m-1]


m = 5
n = 1000

print(uniquePaths(m, n))