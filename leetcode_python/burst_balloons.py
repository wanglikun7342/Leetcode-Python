from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        full_nums = [1]
        for num in nums:
            full_nums.append(num)
        full_nums.append(1)
        dp = [[0 for _ in range(0, len(full_nums))] for _ in range(0, len(full_nums))]
        for length in range(2, len(full_nums)):
            for i in range(0, len(full_nums) - length):
                j = i + length
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], full_nums[k] * full_nums[i] * full_nums[j] + dp[i][k] + dp[k][j])
        return dp[0][len(dp) - 1]


if __name__ == '__main__':
    input_value = [3, 1, 5, 8]
    solution = Solution()
    print(solution.maxCoins(input_value))
