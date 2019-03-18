from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_of_a = max(A)
        min_of_a = min(A)
        result = max_of_a - min_of_a - K * 2 if max_of_a - min_of_a - K * 2 >= 0 else 0
        return result


if __name__ == '__main__':
    solution = Solution()
    A = [1, 3, 6]
    K = 3
    print(solution.smallestRangeI(A, K))
