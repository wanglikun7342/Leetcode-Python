from typing import List

import sys


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        letters = [[0 for _ in range(ord('z') - ord('a') + 1)] for _ in range(len(A))]
        result = []
        for index, str in enumerate(A):
            for ch in str:
                letters[index][ord(ch) - ord('a')] += 1

        for j in range(len(letters[0])):
            min_no = sys.maxsize
            for i in range(len(letters)):
                if letters[i][j] < min_no:
                    min_no = letters[i][j]
            for index in range(0, min_no):
                result.append(chr(ord('a') + j))
        return result


if __name__ == '__main__':
    input = ["bella", "label", "roller"]
    solution = Solution()
    print(solution.commonChars(input))
