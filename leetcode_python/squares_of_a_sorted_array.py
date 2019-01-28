class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            A[i] = pow(A[i], 2)
        return sorted(A)


if __name__ == '__main__':
    array = [-4, -1, 0, 3, 10]
    solution = Solution()
    print(solution.sortedSquares(array))
