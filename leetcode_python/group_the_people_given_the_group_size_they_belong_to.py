from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        val_dict = {}
        result = []
        for index, group_size in enumerate(groupSizes):
            li: List = val_dict.get(group_size)
            if li is None:
                li = [index]
                val_dict[group_size] = li
            else:
                li.append(index)
            if len(li) == group_size:
                result.append(li)
                val_dict[group_size] = None
            else:
                val_dict[group_size] = li
        return result

if __name__ == '__main__':
    groupSizes = [2, 1, 3, 3, 3, 2]
    solution = Solution()
    print(solution.groupThePeople(groupSizes))
