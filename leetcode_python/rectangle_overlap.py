from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = rec1[0]
        y1 = rec1[1]
        x2 = rec1[2]
        y2 = rec1[3]

        x3 = rec2[0]
        y3 = rec2[1]
        x4 = rec2[2]
        y4 = rec2[3]

        if x3 <= x1 < x4:
            if y3 <= y1 < y4:
                return True
            elif y1 >= y4:
                return False
            else:
                if y2 > y3:
                    return True
                else:
                    return False
        elif x1 >= x4:
            return False
        else:
            if x2 > x3:
                if y3 <= y1 < y4:
                    return True
                elif y1 >= y4:
                    return False
                else:
                    if y2 > y3:
                        return True
                    else:
                        return False
            else:
                return False


if __name__ == '__main__':
    rec1 = [-7,-3,10,5]
    rec2 = [-6,-5,5,10]
    solution = Solution()
    isRectangleOverlap = solution.isRectangleOverlap(rec1, rec2)
    print(isRectangleOverlap)
