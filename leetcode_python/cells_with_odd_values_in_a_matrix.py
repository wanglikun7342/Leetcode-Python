from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row_num = [0 for _ in range(0, n)]
        col_num = [0 for _ in range(0, m)]
        for el in indices:
            r =  el[0]
            c = el[1]
            row_num[r] += 1
            col_num[c] += 1
        ans = 0
        for i in range(0, n):
            for j in range(0, m):
                if (row_num[i] + col_num[j]) % 2 == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    input_n = 2
    input_m = 3
    input_indices = [[0, 1], [1, 1]]
    solution = Solution()
    print(solution.oddCells(input_n, input_m, input_indices))
