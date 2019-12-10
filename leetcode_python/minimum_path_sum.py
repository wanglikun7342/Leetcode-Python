from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(0, len(grid[0]))] for _ in range(0, len(grid))]
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[0][j] = dp[0][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][0] = dp[i - 1][0] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[len(dp) - 1][len(dp[0]) - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    solution = Solution()
    print(solution.minPathSum(grid))
