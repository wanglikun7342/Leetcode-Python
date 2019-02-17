class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        a_sum = sum(x for x in A if x % 2 == 0)
        for query in queries:
            val = query[0]
            index = query[1]
            if A[index] % 2 == 0:
                a_sum -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                a_sum += A[index]
            result.append(a_sum)
        return result

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    solution = Solution()
    print(solution.sumEvenAfterQueries(A, queries))
