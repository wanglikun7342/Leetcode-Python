class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sum_L = 0
        sum_R = 0
        result = 0
        for ch in s:
            if ch == 'L':
                sum_L += 1
            elif ch == 'R':
                sum_R += 1
            if sum_R != 0 and sum_L != 0 and sum_R == sum_L:
                result += 1
                sum_L = 0
                sum_R = 0
        return result
