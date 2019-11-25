from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[len(A) - 1] - A[0]
        for index in range(1, len(A)):
            res = min(res, max(A[len(A) - 1] - K, A[index - 1] + K) - min(A[0] + K, A[index] - K))
        return res


if __name__ == '__main__':
    A = [1, 3, 6]
    K = 3
    solution = Solution()
    print(solution.smallestRangeII(A, K))
