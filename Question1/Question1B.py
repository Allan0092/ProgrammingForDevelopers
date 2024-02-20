"""
We can solve this problem using dynamic programming. 
We will create a 2D array dp[i][j], where dp[i][j] represents the minimum time needed to build the first i engines using j engineers. 
The base case is dp[0][0] = 0, as no engines need to be built by no engineers.

We will iterate through the number of engines i and the number of engineers j,
For each engine and engineer we have 2 options:

1. The last engineer works on building the i-th engine. 
So the time cost is the time cost of building the (i-1)-th engine plus the time cost of building the i-th engine.

2. The last engineer splits into two engineers.
So the time cost is the time cost of building the (i-1)-th engine plus the time cost of splitting the last engineer.

Finally we will get the minimum of the above two options.

"""



def min_time_to_build_engine(engines: list[int], split: int):
    """returns the minimum time for the engineers to work on the engines.

    Args:
        engines (list[int]): the list of engines
        split (int): split cost

    Returns:
        int: the minimum type requires
    """
    n = len(engines) # Get the total number of engines
    dp = [[0] * (n + 1) for _ in range(n + 1)] # initialize dp with the number of engines
    for i in range(1, n + 1): # iterate through each engine
        for j in range(1, n + 1): # iterate though engineers
            if j == 1:
                dp[i][j] = dp[i - 1][j] + engines[i - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + engines[i - 1], dp[i - 1][j] + split)
    return dp[n][n]


def main():
    # The given input
    engines: list[int] = [1, 2, 3]
    split_cost = 1
    print(min_time_to_build_engine(engines, split_cost)) # Output 3

if __name__=="__main__":
    main()