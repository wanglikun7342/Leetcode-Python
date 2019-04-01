from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        rels = {}
        for index, equation in enumerate(equations):
            x = equation[0]
            y = equation[1]
            if x in rels:
                rels[x][y] = values[index]
            else:
                rels[x] = {y: values[index]}
            if y in rels:
                rels[y][x] = 1.0 / values[index]
            else:
                rels[y] = {x: 1.0 / values[index]}

        for rel in rels.values():
            for x in rel.keys():
                for y in rel.keys():
                    rels[x][y] = rel[y] / rel[x]
                    rels[y][x] = rel[x] / rel[y]

        for query in queries:
            if query[0] in rels:
                x = rels[query[0]]
                y = x.get(query[1], -1.0)
                result.append(y)
            else:
                result.append(-1.0)
        return result


if __name__ == '__main__':
    solution = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(solution.calcEquation(equations, values, queries))
