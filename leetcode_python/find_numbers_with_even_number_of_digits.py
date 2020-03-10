from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                sum += 1
        return sum


if __name__ == '__main__':
    input_nums = [12, 345, 2, 6, 7896]
    solution = Solution()
    print(solution.findNumbers(input_nums))
