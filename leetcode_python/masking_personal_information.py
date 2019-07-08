import re


class Solution:
    def maskPII(self, S: str) -> str:
        if "@" in S:
            at_index = S.index("@")
            return (S[0] + "*****" + S[at_index - 1] + S[at_index:]).lower()
        else:
            S = re.sub("\D", "", S)
            if len(S) == 10:
                return "***-***-" + S[len(S) - 4:]
            else:
                ans = "+"
                for i in range(0, len(S) - 10):
                    ans += "*"
                return ans + "-" + "***-***-" + S[len(S) - 4:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maskPII("1(234)567-890"))
