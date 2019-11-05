from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif j - 1 < 0:
                    dp[i][j] = dp[i - 1][j]
                elif i - 1 < 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == '__main__':
    input_array = [[0, 1]]
    solution = Solution()
    print(solution.uniquePathsWithObstacles(input_array))
