from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        ans = float('inf')
        left = 0
        right = sum(nums) + 1
        while left < right:
            mid = (left + right) // 2
            if self.__guess(nums, m, mid):
                ans = mid
                right = mid
            else:
                left = mid + 1

        return ans

    def __guess(self, nums, m, mid):
        sum_val = 0
        for num in nums:
            if num + sum_val > mid:
                m-=1
                sum_val = num
                if num > mid:
                    return False
            else:
                sum_val += num
        return m >= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.splitArray([1, 4, 4], 3))
