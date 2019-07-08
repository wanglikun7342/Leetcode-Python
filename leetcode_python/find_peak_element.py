from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.__findPeakElement(nums, 0, len(nums) - 1)

    def __findPeakElement(self, nums: List[int], startIndex: int, endIndex: int):
        midIndex = (endIndex + startIndex) // 2
        midVal = nums[midIndex]
        leftIndex = midIndex - 1
        if midIndex == 0:
            leftVal = float('-inf')
        else:
            leftVal = nums[leftIndex]

        rightIndex = midIndex + 1
        if midIndex == len(nums) - 1:
            rightVal = float('-inf')
        else:
            rightVal = nums[rightIndex]
        if midVal > leftVal and midVal > rightVal:
            return midIndex
        elif midVal < leftVal:
            return self.__findPeakElement(nums, startIndex, leftIndex)
        else:
            return self.__findPeakElement(nums, rightIndex, endIndex)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement([1, 2, 3, 1]))
