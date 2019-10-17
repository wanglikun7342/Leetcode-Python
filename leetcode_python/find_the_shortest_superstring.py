from typing import List


class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        while len(A) > 1:
            x = 0
            y = 1
            for iv_index, iv_value in enumerate(A):
                for index in range(iv_index + 1, len(A)):
                    if self.__get_over_lapping(iv_value, A[index]) > self.__get_over_lapping(A[x], A[y]):
                        x = iv_index
                        y = index
            a = A[x]
            b = A[y]
            A.remove(a)
            A.remove(b)
            A.append(self.__get_over_lapping_string(a, b))
        return A[0]

    def __get_over_lapping(self, x, y):
        return len(x) + len(y) - len(self.__get_over_lapping_string(x, y))

    def __get_over_lapping_string(self, str1, str2):
        result = ""
        for iv_index, iv_value in enumerate(str1):
            if iv_value != str2[0]:
                continue
            continue_flag = False
            for index in range(iv_index, len(str1)):
                if str1[index] != str2[index - iv_index]:
                    continue_flag = True
                    break
            if continue_flag:
                continue
            result = str1 + str2[len(str1) - iv_index:]
            break
        for iv_index, iv_value in enumerate(str2):
            if iv_value != str1[0]:
                continue
            continue_flag = False
            for index in range(iv_index, len(str2)):
                if str2[index] != str1[index - iv_index]:
                    continue_flag = True
                    break
            if continue_flag:
                continue
            newResult = str2 + str1[len(str2) - iv_index:]
            if len(newResult) < len(result) or result == "":
                result = newResult
            break
        if result == "":
            result = str1 + str2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestSuperstring(["gruuz", "zjr", "uuzj", "rfgr"]))
