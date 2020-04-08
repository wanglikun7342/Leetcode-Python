from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        avg = sum(A) // 3
        total = 0
        times = 0
        for num in A:
            total += num
            if total == avg:
                total = 0
                times += 1
        return times == 3 or (times > 3 and avg == 0)


if __name__ == '__main__':
    input_arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    solution = Solution()
    solution.canThreePartsEqualSum(input_arr)
