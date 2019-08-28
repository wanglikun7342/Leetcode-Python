class Solution:
    def customSortString(self, S: str, T: str) -> str:
        char_map = {}
        for el in S:
            char_map[el] = 0
        for el in T:
            if el in char_map:
                char_map[el] = char_map[el] + 1
            else:
                char_map[el] = 1
        output_str = ""
        for el in char_map.keys():
            num = char_map[el]
            for i in range(0, num):
                output_str += el
        return output_str


if __name__ == '__main__':
    S = "cba"
    T = "abcd"
    solution = Solution()
    result = solution.customSortString(S, T)
    print(result)
