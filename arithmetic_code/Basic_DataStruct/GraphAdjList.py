class GraphAdjList:

    def __init__(self) -> None:
        self.vertex = []
        self.edges = {}

    def add_vertex(self, vet):
        if vet in self.vertex:
            raise IndexError()

        self.vertex.append(vet)
        self.edges[vet] = []

    def add_edges(self, vet1, vet2):
        if vet1 not in self.vertex or vet2 not in self.vertex or vet1 == vet2:
            raise IndexError()

        self.edges[vet1].append(vet2)
        self.edges[vet2].append(vet1)

    def delete_vertex(self, vet):
        if vet not in self.vertex:
            raise IndexError()

        self.edges.pop(vet, 0)
        for val in self.edges.values():
            if vet in val:
                index = val.index(vet)
                val.pop(index)

    def delete_edge(self, vet1, vet2):
        if vet1 not in self.vertex or vet2 not in self.vertex or vet1 == vet2:
            raise IndexError()
        if vet2 not in self.edges[vet1]:
            raise IndexError

        index1 = self.edges[vet1].index(vet2)
        index2 = self.edges[vet2].index(vet1)
        self.edges[vet1].pop(index1)
        self.edges[vet2].pop(index2)

    def print(self):
        print("邻接表：", end=' ')
        print(self.vertex)
        print("邻接表:")
        for k, v in self.edges.items():
            print(k, v)

    def BFS(self):
        cur = self.vertex
        queue = [cur[0]]
        visited = set()
        visited.add(cur[0])
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            lst_node = self.edges[node]
            for i in lst_node:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return res

    def dfs(self):
        res = []
        visited = set()
        self.dfs_helper(visited, res, self.vertex[0])
        return res

    def dfs_helper(self, visited, res, vet):
        res.append(vet)
        visited.add(vet)
        lst_node = self.edges[vet]
        for i in lst_node:
            if i not in visited:
                self.dfs_helper(visited, res, i)


x = [1, 2, 5, 4, 3]
edges = [[1, 3], [1, 5], [3, 2], [2, 5], [2, 4], [5, 4]]

graph = GraphAdjList()

for i in x:
    graph.add_vertex(i)
for edge in edges:
    graph.add_edges(edge[0], edge[1])
# graph.print()
# graph.add_vertex(6)
# graph.print()
# graph.add_edges(1, 6)
# graph.print()
# graph.delete_edge(2, 5)
# graph.print()
# graph.delete_vertex(1)
# graph.print()
print(graph.BFS())
print(graph.dfs())