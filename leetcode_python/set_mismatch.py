from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for val in nums:
            num = abs(val)
            if nums[num - 1] < 0:
                result.append(num)
            else:
                nums[num - 1] *= -1
            total += num
        result.append(len(nums) * (len(nums) + 1) // 2 - total + result[0])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findErrorNums([2, 2]))
