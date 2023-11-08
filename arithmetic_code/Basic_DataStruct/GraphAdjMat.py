class GrapgAdjMat:

    def __init__(self, vertex: 'list[int]', edges: 'list[list[int]]') -> None:
        """
        vertex:是一个列表存放节点：[2,5,3,1,4]
        edges:是2维列表:[[2,4],[2,5],[1,3]]，存放节点与节点的边
        """
        self.vertex = []
        self.edge = []
        for vet in vertex:
            self.add_vertex(vet)
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        return len(self.vertex)

    def add_vertex(self, vertex: 'int') -> None:
        n = self.size()
        if vertex in self.vertex:
            raise IndexError()

        new_row = [0] * n
        self.vertex.append(vertex)
        self.edge.append(new_row)
        for row in self.edge:
            row.append(0)

    def add_edge(self, vet1: 'int', vet2: 'int'):
        if vet1 not in self.vertex or vet2 not in self.vertex or vet1 == vet2:
            raise IndexError()

        index1 = self.vertex.index(vet1)
        index2 = self.vertex.index(vet2)
        self.edge[index1][index2] = 1
        self.edge[index2][index1] = 1

    def delete_vertex(self, vertex):
        if vertex not in self.vertex:
            raise IndexError()
        index = self.vertex.index(vertex)
        self.vertex.pop(index)
        self.edge.pop(index)
        for row in self.edge:
            row.pop(index)

    def delete_edge(self, vet1, vet2):
        if vet1 not in self.vertex or vet2 not in self.vertex or vet1 == vet2:
            raise IndexError()

        index1 = self.vertex.index(vet1)
        index2 = self.vertex.index(vet2)
        self.edge[index1][index2] = 0
        self.edge[index2][index1] = 0

    def print(self):
        print("节点列表：")
        print(self.vertex)
        print("邻接矩阵：")
        for row in self.edge:
            print(row)

    def BFS(self):
        """
        邻接矩阵的遍历
        """
        res = []
        cur_point = self.vertex[:]
        visited = set()
        queue = [cur_point[0]]
        visited.add(cur_point[0])
        while queue:
            vet = queue.pop(0)
            index = cur_point.index(vet)
            res.append(vet)
            lst_edge = self.edge[index]
            for i in range(len(lst_edge)):
                if lst_edge[i] != 0 and self.vertex[i] not in visited:
                    queue.append(self.vertex[i])
                    visited.add(self.vertex[i])
        return res

    def DFS(self):
        res = []
        visited = set()
        start_vet = self.vertex[0]
        self.dfs_helper(visited, res, start_vet)
        return res

    def dfs_helper(self, visited, res, vet):
        res.append(vet)
        visited.add(vet)
        index = self.vertex.index(vet)
        lst_edge = self.edge[index]
        for i in range(len(lst_edge)):
            if lst_edge[i] != 0 and self.vertex[i] not in visited:
                self.dfs_helper(visited, res, self.vertex[i])


x = [0, 1, 3, 2, 5, 4, 6]
edge = [[0, 1], [0, 3], [1, 2], [2, 5], [5, 4], [5, 6]]
graph = GrapgAdjMat(x, edge)
# graph.print()
# graph.delete_edge(1, 5)
# graph.print()
# graph.add_vertex(6)
# graph.print()
# graph.add_edge(6, 3)
# graph.print()
print(graph.BFS())
print(graph.DFS())
