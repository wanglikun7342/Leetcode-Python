from typing import List

class Solution:
    color = []
    graph = []

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        self.graph = graph
        self.color = [0 for _ in range(0, len(graph))]
        for node in range(0, len(graph)):
            if self.dfs(node):
                result.append(node)
        return result

    def dfs(self, node: int) -> bool:
        if self.color[node] > 0:
            return self.color[node] == 2
        self.color[node] = 1
        for subnode in self.graph[node]:
            if not self.dfs(subnode):
                return False

        self.color[node] = 2
        return True


if __name__ == '__main__':
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    solution = Solution()
    print(solution.eventualSafeNodes(graph))
