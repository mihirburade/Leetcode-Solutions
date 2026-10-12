class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue

                top=dp[i-1][j] if i>0 else 0
                left=dp[i][j-1] if j>0 else 0
                dp[i][j]=top+left

                if  obstacleGrid[i][j]==1:
                    dp[i][j]=0

        return dp[m-1][n-1]
