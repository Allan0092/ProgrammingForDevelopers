def convertToDict(edges: list) -> dict:
    nodes = {}
    for i in edges:
        if i[0] in nodes:
            value =  nodes.get(i[0])
            value.append(i[1])
            nodes[i[0]] = value
        else:
            nodes[i[0]] = [i[1]]
    return nodes


def convertToUndirectedDict(edges: list) -> dict:
    nodes = {}
    for i in edges:
        nodes[i[0]] = set()
        nodes[i[1]] = set()
    for i in edges:
        node1 = nodes.get(i[0])
        node1.add(i[1])
        node2 = nodes.get(i[1])
        node2.add(i[0])
        nodes[i[0]] = node1
        nodes[i[1]] = node2
    for i in edges:
        value =  nodes.get(i[0])
        value.add(i[1])
        nodes[i[0]] = value
    for i in nodes:
        value = nodes.get(i)
        nodes[i] = list(value)
    return nodes


def getAffectedList(target: int, nodes: dict) -> list:
    if target not in nodes:
        return []
    affected = nodes.get(target)
    affected_copy = affected.copy()
    for i in nodes:
        for j in affected:
            if j in nodes.get(i) and j in affected_copy and (i != target):
                affected_copy.pop(affected_copy.index(j))
    return affected_copy


def getAllNodes(edges: list) -> set:
    all_edges = set()
    for i in edges:
        for j in i:
            all_edges.add(j)
    return all_edges


def getAffected(edges: list, target: int=-1):
    nodes: dict = convertToUndirectedDict(edges)
    visited = []
    
    def dfs(nodes: dict, current: int):
        if current in visited or current == target:
            return
        visited.append(current)
        print(current)
        for neighbor in nodes.get(current, []):
            dfs(nodes, neighbor)
    
    dfs(nodes, edges[0][0])
    return visited





def main():
    edges = [[0, 1], [0, 2], [1, 3], [1, 6], [2, 4], [4, 6], [4, 5], [5, 7]]
    target = 4
    # a = convertToDict(edges)
    # print(a)
    # print(getAffectedList(target, a))
    # print(getAllNodes(edges))
    # print(convertToUndirectedDict(edges))
    getAffected(edges)


if __name__ == "__main__":
    main()