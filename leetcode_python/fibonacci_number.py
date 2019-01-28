class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        fib_list = [0, 1]
        for index in range(2, N + 1):
            fib_list.append(fib_list[index - 1] + fib_list[index - 2])
        return fib_list[N]


if __name__ == '__main__':
    num = 3
    solution = Solution()
    print(solution.fib(num))
