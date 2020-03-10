from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bit_mask = 0
        for num in nums:
            bit_mask = bit_mask ^ num
        bit_pos = bit_mask & (-bit_mask)
        x = 0
        for num in nums:
            if bit_pos & num != 0:
                x = x ^ num
        return [x, bit_mask ^ x]


if __name__ == '__main__':
    input_arr = [1, 2, 1, 3, 2, 5]
    solution = Solution()
    print(solution.singleNumber(input_arr))
