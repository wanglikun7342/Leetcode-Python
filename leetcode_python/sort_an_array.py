from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.__quick_sort(nums, 0, len(nums) - 1)
        return nums

    def __quick_sort(self, nums, start, end):
        if start > end:
            return
        head = start
        tail = end
        while head < tail:
            while head < tail and nums[tail] >= nums[start]:
                tail -= 1
            while head < tail and nums[head] <= nums[start]:
                head += 1
            if head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
        nums[head], nums[start] = nums[start], nums[head]
        self.__quick_sort(nums, start, head - 1)
        self.__quick_sort(nums, head + 1, end)


if __name__ == '__main__':
    input_arr = [5, 1, 1, 2, 0, 0]
    solution = Solution()
    print(solution.sortArray(input_arr))
