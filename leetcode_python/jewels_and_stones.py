class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for j in J:
            sum = sum+S.count(j)
        return sum

if __name__ == '__main__':
    J = "aA"
    S = "aAAAbbbbb"
    solution = Solution()
    print(solution.numJewelsInStones(J,S))
