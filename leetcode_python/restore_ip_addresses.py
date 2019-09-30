from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) == 0 or len(s) > 12:
            return []
        result = []
        self._dfs(s, 0, "", result, 0)
        return result

    def _dfs(self, s, end, ip, result, count):
        for start in range(end, end + 3):
            ip_segment = s[end:start+1]
            if len(ip_segment) > 1 and ip_segment[0] == '0':
                break
            if int(ip_segment) > 255:
                break
            if start == len(s) - 1:
                if count == 3:
                    result.append(ip + "." + ip_segment)
                break
            if ip != "":
                self._dfs(s, start + 1, ip + "." + ip_segment, result, count+1)
            else:
                self._dfs(s, start + 1, ip_segment, result, count+1)

if __name__ == '__main__':
    input_str = "25525511135"
    solution = Solution()
    solution.restoreIpAddresses(input_str)
    i = 1
