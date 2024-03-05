class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class MinHeap:
    def __init__(self):
        self.heap = []


    def parent(self, i):
        return (i - 1) // 2


    def left(self, i):
        return 2 * i + 1


    def right(self, i):
        return 2 * i + 2


    def insert(self, edge):
        self.heap.append(edge)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)].weight > self.heap[i].weight:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_heapify(0)
        return root


    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.heap) and self.heap[l].weight < self.heap[smallest].weight:
            smallest = l
        if r < len(self.heap) and self.heap[r].weight < self.heap[smallest].weight:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

if __name__ == "__main__":
    graph = [
        Edge(0, 1, 10),
        Edge(0, 2, 6),
        Edge(0, 3, 5),
        Edge(1, 3, 15),
        Edge(2, 3, 4)
    ]
    minHeap = MinHeap()
    minHeap.insert(graph)