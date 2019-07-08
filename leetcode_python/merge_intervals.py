from typing import List


def cmp(x, y):
    return x-y

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals)
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
            else:
                lastInterval: List = result[(len(result) - 1)]
                if lastInterval[1] < interval[0]:
                    result.append(interval)
                else:
                    if lastInterval[0] > interval[0]:
                        lastInterval[0] = interval[0]
                    if interval[1] > lastInterval[1]:
                        lastInterval[1] = interval[1]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 4], [0, 0]]))
