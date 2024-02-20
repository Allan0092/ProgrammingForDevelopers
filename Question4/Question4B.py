""" 
For this problem we need to treverse through the nodes in a inorder form,
while triversing we will use the max-heap queue to get the maximum difference
between target and the current node's data.
if the difference is small,
we will replace the higher value in the max-heap with the new node.data and its difference

the max-heap will store data in the form [node.data, difference]

"""


import sys # for getting the infiny integer
import heapq # for implementing max-heap data structure


class Node: # a node class
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def get_closest(root: Node, k, x):
    """gets the closest x number of values to the target k in the Node root

    Args:
        root (Node): root node
        k (int): the target
        x (int): the number of values closest to k

    Returns:
        list[int]: the list of closest number of values to the target
    """
    # following three lines will initialize a list of x length with values [-1, -infinity] and create a max-heap
    closest_values: list[list[int, int]] = [] 
    [closest_values.append([-1, -sys.maxsize]) for _ in range(x)]
    heapq.heapify(closest_values)
    def inOrder(root: Node):
        if root == None:
            return
        inOrder(root.left)
        if (abs(k-root.data))<abs(closest_values[0][1]): # if the current node's data's difference with the target is lower than the highest difference in max-heap
            heapq.heappop(closest_values) # remove the highest difference
            heapq.heappush(closest_values, [root.data, k-root.data]) # add the new value
        inOrder(root.right)
    inOrder(root)
    return [i[0] for i in closest_values] # returns the first index


def main():
    # Given inputs
    root = Node(4)
    
    root.left = Node(2)
    root.right = Node(5)
    
    root.left.left = Node(1)
    root.left.right = Node(3)

    x: int = 2 # the closest x values
    k: int = 3.8 # the target

    print(get_closest(root, k, x)) # output: [3, 4]


if __name__ == "__main__":
    main()