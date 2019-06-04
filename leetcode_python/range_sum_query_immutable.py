from typing import List


class NumArray:
    sums = []

    def __init__(self, nums: List[int]):
        self.sums.append(0)
        for index in range(0, len(nums)):
            self.sums.append(self.sums[index] + nums[index])

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    num_array = NumArray([-1])
    output = num_array.sumRange(0,0)
    print(output)
