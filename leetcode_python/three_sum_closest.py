from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result_sum = nums[0] + nums[1] + nums[2]
        nums.sort()
        for x in range(len(nums)):
            i = x + 1
            j = len(nums) - 1
            while i < j:
                cur_sum = nums[x] + nums[i] + nums[j]
                cur_diff = abs(cur_sum - target)
                diff = abs(result_sum - target)
                if cur_diff < diff:
                    result_sum = cur_sum
                if cur_sum - target > 0:
                    j -= 1
                elif cur_sum - target < 0:
                    i += 1
                else:
                    return result_sum
        return result_sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-3,-2,-5,3,-4], -1))
