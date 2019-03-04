from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        result = []
        pre = float('-inf')
        for index, ch in enumerate(S):
            if ch == C:
                pre = index
            result.append(index - pre)

        pre = float('inf')
        for index in range(len(S) - 1, -1, -1):
            if S[index] == C:
                pre = index
            result[index] = min(result[index], pre - index)

        return result


if __name__ == '__main__':
    solution = Solution()
    S = "loveleetcode"
    C = "e"
    print(solution.shortestToChar(S, C))
