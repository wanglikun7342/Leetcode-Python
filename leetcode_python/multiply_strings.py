class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result = [0 for _ in range(len(num1) + len(num2))]
        for index_1 in range(len(num1) - 1, -1, -1):
            for index_2 in range(len(num2) - 1, -1, -1):
                mul = int(num1[index_1]) * int(num2[index_2])
                s = mul // 10
                g = mul % 10
                pos = len(result) - 1 - (len(num1) - 1 -index_1 +len(num2) - 1 -index_2)
                result[pos] += g
                if result[pos] >= 10:
                    result[pos] = result[pos] % 10
                    result[pos - 1] += 1
                result[pos - 1] += s
                if result[pos - 1] >= 10:
                    result[pos - 1] = result[pos - 1] % 10
                    result[pos - 2] += 1
        sb = ""
        index = 0
        for i in range(len(result)):
            if result[i] != 0:
                index = i
                break
        for i in range(index, len(result)):
            sb += str(result[i])
        return sb


if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply("2", "3"))
