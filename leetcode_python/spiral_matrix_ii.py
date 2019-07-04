from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(0, n)] for _ in range(0, n)]
        i = 0
        j = 0
        dj = 1
        di = 0
        value = 1
        while value <= n * n:
            result[i][j] = value
            value += 1
            j += dj
            i += di
            if j >= n or i >= n or j < 0 or i <0 or result[i][j] != 0:
                j-=dj
                i-=di
                if dj == 1 :
                    dj = 0
                    di = 1
                elif dj == -1 :
                    dj = 0
                    di = -1
                elif di == 1:
                    dj = -1
                    di = 0
                elif di == -1:
                    dj = 1
                    di = 0
                j+=dj
                i+=di
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(3))
