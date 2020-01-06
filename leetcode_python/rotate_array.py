from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        length = len(nums)
        self.__reverse(nums, 0, length - 1)
        self.__reverse(nums, 0, k - 1)
        self.__reverse(nums, k, length - 1)

    def __reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            start += 1
            nums[end] = temp
            end -= 1


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4, 5, 6, 7]
    solution = Solution()
    solution.rotate(input_nums, 3)
    print(input_nums)
