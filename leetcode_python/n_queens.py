from typing import List


class Solution:
    results = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results.clear()
        area = [[0 for _ in range(0, n)] for _ in range(0, n)]
        for col in range(0, n):
            self.__reset(area, 0)
            self.__place(area, 0, col)

        return self.results

    def __output(self, area):
        result = []
        for row in range(0, len(area)):
            line = ""
            for col in range(0, len(area[0])):
                if area[row][col] != 1:
                    line += "."
                else:
                    line += "Q"
            result.append(line)
        self.results.append(result)

    def __reset(self, area, index):
        for row in range(index, len(area)):
            for col in range(0, len(area[0])):
                area[row][col] = 0

    def __place(self, area, rowIndex, colIndex):
        area[rowIndex][colIndex] = 1
        for row in range(0, rowIndex):
            if area[row][colIndex] == 1:
                area[rowIndex][colIndex] = 0
                return
            leftCol = rowIndex - row + colIndex
            if 0 <= leftCol <= len(area) - 1:
                if area[row][leftCol] == 1:
                    area[rowIndex][colIndex] = 0
                    return

            rightCol = row - rowIndex + colIndex
            if 0 <= rightCol <= len(area) - 1:
                if area[row][rightCol] == 1:
                    area[rowIndex][colIndex] = 0
                    return

        for col in range(0, len(area[0])):
            newRow = rowIndex + 1
            if newRow == len(area):
                self.__output(area)
                return
            self.__reset(area, newRow)
            self.__place(area, newRow, col)


if __name__ == '__main__':
    solution = Solution()
    solution.solveNQueens(4)
