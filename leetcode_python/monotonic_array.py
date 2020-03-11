from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return True
        if A[0] < A[len(A) - 1]:
            for index in range(1, len(A)):
                if A[index] - A[index - 1] < 0:
                    return False
            return True
        else:
            for index in range(1, len(A)):
                if A[index] - A[index - 1] > 0:
                    return False
            return True
