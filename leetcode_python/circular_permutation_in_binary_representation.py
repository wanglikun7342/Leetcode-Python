from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        vis = [False for _ in range(0, 1 << n)]
        ans = [start]
        vis[start] = True
        cur = start
        for i in range(0, 1 << n):
            for j in range(0, n):
                t = cur ^ (1 << j)
                if vis[t] is not True:
                    vis[t] = True
                    ans.append(t)
                    cur = t
                    break
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.circularPermutation(3, 2))
