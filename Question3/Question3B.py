class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet:
    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]
        self.rank = [0] * vertices

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def kruskal_mst(graph):
    vertices = len(graph)
    result = []  # List to store the MST edges

    # Create edges from the graph
    edges = []
    for u in range(vertices):
        for v, weight in graph[u]:
            edges.append(Edge(u, v, weight))

    # Sort edges by weight
    edges.sort()

    # Create disjoint-set data structure
    disjoint_set = DisjointSet(vertices)

    # Iterate through sorted edges
    for edge in edges:
        u, v, weight = edge.source, edge.destination, edge.weight

        # Check if adding the edge creates a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            result.append(edge)
            disjoint_set.union(u, v)

    return result


# Example usage
graph = [
    [(1, 4), (2, 8)],
    [(0, 4), (2, 11)],
    [(0, 8), (1, 11), (3, 2)],
    [(2, 2)],
]

mst = kruskal_mst(graph)

# Print the MST
for edge in mst:
    print(f"{edge.source} -> {edge.destination} ({edge.weight})")
