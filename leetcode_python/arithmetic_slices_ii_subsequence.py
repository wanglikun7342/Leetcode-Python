from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        result = 0
        cnt = [{} for _ in range(0, len(A))]
        for i in range(0, len(A)):
            for j in range(0, i):
                delta = A[i] - A[j]
                diff = delta
                s = cnt[j].get(diff, 0)
                origin = cnt[i].get(diff, 0)
                cnt[i][diff] = origin + s + 1
                result += s
        return result


if __name__ == '__main__':
    input_array = [2, 4, 6, 8, 10]
    solution = Solution()
    print(solution.numberOfArithmeticSlices(input_array))
