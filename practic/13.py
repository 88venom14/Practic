from collections import deque
from typing import List, Optional

class Graph:
    def __init__(self, n: int, edges: Optional[List[tuple]] = None, use_matrix: bool = False):
        self.n = n
        self.use_matrix = use_matrix

        if use_matrix:
            self.matrix = [[0] * n for _ in range(n)]
            self.adj_list = None
        else:
            self.adj_list = [[] for _ in range(n)]
            self.matrix = None

        if edges:
            for u, v in edges:
                self.add_edge(u, v)

    def add_edge(self, u: int, v: int):
        if self.use_matrix:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1
        else:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def _get_neighbors(self, u: int) -> List[int]:
        if self.use_matrix:
            return [v for v in range(self.n) if self.matrix[u][v] == 1]
        else:
            return self.adj_list[u]

    def bfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        queue = deque([start])
        visited[start] = True
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in self._get_neighbors(u):
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        order = []

        def _dfs(u):
            visited[u] = True
            order.append(u)
            for v in self._get_neighbors(u):
                if not visited[v]:
                    _dfs(v)
        _dfs(start)
        return order

    def shortest_path(self, start: int, end: int) -> int:
        if start == end:
            return 0

        visited = [False] * self.n
        queue = deque([(start, 0)])
        visited[start] = True

        while queue:
            u, dist = queue.popleft()
            for v in self._get_neighbors(u):
                if v == end:
                    return dist + 1
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, dist + 1))
        return -1

if __name__ == "__main__":

    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    n = 5

    print("1. Список смежности:")
    g_list = Graph(n, edges, use_matrix=False)
    print("  BFS из вершины 0:", g_list.bfs(0))
    print("  DFS из вершины 0:", g_list.dfs(0))
    print("  Кратчайший путь 0 -> 4:", g_list.shortest_path(0, 4))

    print("\n2. Матрица смежности:")
    g_matrix = Graph(n, edges, use_matrix=True)
    print("  BFS из вершины 0:", g_matrix.bfs(0))
    print("  DFS из вершины 0:", g_matrix.dfs(0))
    print("  Кратчайший путь 0 -> 4:", g_matrix.shortest_path(0, 4))

    print("\n3. Проверка недостижимости (вершина 0 -> 5 в графе из 5 вершин):")
    print("  Результат:", g_list.shortest_path(0, 5))