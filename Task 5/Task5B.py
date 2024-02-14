"""
This probem can be solved using the depth first traversal of nodes.

First let us convert the given input of edge list into a 
dictionary with {key: [value}} pair of {node: [node, node, ...]}.
This is achieved using the convertToUndirectedDict() function.

Then we can first trverse through the nodes by depth first traverse
before the power outage occurs, and save it as a set.
Again traverse through the nodes using depth first traverse without 
travelling to the target node and save it as a set.
I implemented the depth first traverse using iteration at 
depthFirstTraverse() function.

Lastly using the set's property of difference to find out
which nodes are absent in the second set to get the affected nodes list.
"""

def convertToUndirectedDict(edges: list) -> dict:
    """converts the list of connected edges to a dictionary of connected
        nodes in the form {u: [v, v, ..]} for undirected graphs.

    Args:
        edges [[],[]]: the list of connected edges.

    Returns:
        dict: dictionary of connected nodes.
    """
    nodes = {} # initializing a dictionary.
    for i in edges: # iterate and add a new node in the dictionary.
        nodes[i[0]] = set([i[1]]) # initialize a set with value of its connected node
        nodes[i[1]] = set([i[0]]) #  initialize a set with value of its connected node
    for i in edges: # iterate through each connected edges to add new connected node.
        value =  nodes.get(i[0])
        value.add(i[1]) # to avoid duplication, set is used.
        nodes[i[0]] = value
    for i in nodes: # convert set to list
        value = nodes.get(i)
        nodes[i] = list(value)
    return nodes


def depthFirstTraverse(edges: list, target: int=-1) -> list:
    """Using depth first traverse with iteration we visit and 
    save each node and return all the visited nodes as a list.
    If the target is given, we avoid travelling to that node.

    Args:
        edges (list): get the connected edge list.
        target (int, optional): the node with the power outage. Defaults to -1.

    Returns:
        list: list of connected nodes
    """
    nodes: dict = convertToUndirectedDict(edges) # convert the connected 
    if target!=-1:
        visited = [target]
    else:
        visited = []
    
    def dfs(nodes: dict, current: int):
        if current in visited or current == target:
            return
        visited.append(current)
        for neighbor in nodes.get(current, []):
            dfs(nodes, neighbor)
    
    dfs(nodes, edges[0][0])
    return visited


def getAffected(edges: list, target: int) -> list:
    """Get the list of affected nodes due to power outage on the target node.

    Args:
        edges (list): list of connected edges.
        target (int): the node with the power outage.

    Returns:
        list: the list of affected nodes excluding the target node itself.
    """
    without_outage = set(depthFirstTraverse(edges))
    after_outage = set(depthFirstTraverse(edges, target))
    return list(without_outage - after_outage)


def main():
    # test cases
    edges = [[0, 1], [0, 2], [1, 3], [1, 6], [2, 4], [4, 6], [4, 5], [5, 7]]
    target = 4
    print(getAffected(edges, target)) # Output: [5, 7]


if __name__ == "__main__":
    main()