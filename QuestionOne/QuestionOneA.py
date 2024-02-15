"""
First let us find out all the possible ways of decorating the venues with the adjacency constraint in mind.
This is done using the all_possible_themes() function.

Then we can get the respective sum of all the possible combinations.
We can use a dict to easily map out the combination along with the cost.
This is done using the price_of_combination() function.

At last we can find the minimum cost by iterating through the dict that we got from the price_of_combination() function.
This is done through the min_cost() function.
"""
import random # for testing purposes
import sys # to get the infinity integer


def generate_nested_lists(n, c):
    """For testing. Generates a nested list of size n with c number of random integers from range 1 to 15

    Args:
        n (int): number of lists nested in the main list
        c (int): number of int in the nested list

    Returns:
        list[list][int]: a nested list of random generated list.
    """
    nested_list = []
    for _ in range(n):
        inner_list = [random.randint(1, 15) for _ in range(c)]
        nested_list.append(inner_list)
    return nested_list


def min_cost(all_sum: dict) -> int:
    """selects the minimum cost of from all the sum in the dict.

    Args:
        all_sum (dict): should have the key as a list formated to a string and the value should be the sum of the price required to decorate the venue

    Returns:
        int: the lowest cost
    """
    min:int = sys.maxsize # initialize with positive infinity.
    for combination in all_sum: # iterate through each combination.
        if all_sum[str(combination)]<min: # when a new minimum is found.
            min = all_sum[str(combination)] # assign a new minimum.
    return min


def all_possible_themes(costs: list[list[int]]) -> list[list]:
    """Generates all the possible lists of combination and stores the index with respect to the adjacency constraint.

    Args:
        costs (list[list[int]]): the cost of decorating the venue.
    
    Returns:
        list[list]: the list of all possible combinations of themes.
    """
    def generate_combinations(curr_index, prev_index, result):
        if len(curr_index) == len(costs): 
            result.append(curr_index.copy())
            return
        for i in range(len(costs[len(curr_index)])): # loop according to the number of themes in a venue.
            if i != prev_index: # adjacency constraint.
                curr_index.append(i) # add the index to the list.
                generate_combinations(curr_index, i, result)
                curr_index.pop()
    result = [] # initialize with a empty list.
    generate_combinations([], -1, result) # function call
    return result


def price_of_combination(costs: list[list[int]], index_combination: list[list[int]]) -> dict:
    """Calculates the cost of decorating each possible combination themes.

    Args:
        costs (list[list[int]]): The list of cost for decorating the venue.
        index_combination (list[list[int]]): the list of combination of all possible themes.

    Returns:
        dict: key:str(list of themes) value: sum of cost of all themes.
    """
    all_costs = {} # initialize an empty dictionary.
    for venues in index_combination: # get each combination.
        sum_cost = 0 # set the sum of decorating the venues to 0.
        for j, theme in enumerate(venues): # get the index of each individual theme .
            sum_cost+=costs[j][theme] # increment the cost of chosen themes.
        all_costs[str(venues)] = sum_cost # save the combination and the cost in a dictionary.
    return all_costs


def get_lowest_cost_of_decorating_venues(costs: list[list[int]]) -> int:
    """gives the lowest cost of decorating each venues without the adjacent themes matching.

    Args:
        costs (list[list[int]]): the list of venues with the cost of decorating each venues.

    Returns:
        int: minimum cost.
    """
    all_possible_combinations: list[list[int]] = all_possible_themes(costs) # finds out all possible combination of themes.
    combinations_with_cost:dict = price_of_combination(costs, all_possible_combinations) # returns all the cost of each combination.
    lowest_cost:int = min_cost(combinations_with_cost) # returns the lowest cost from each and every combination.
    return lowest_cost


def main():
    costs = [[3, 1, 5], [1, 3, 2], [4, 6, 8]] # given input
    print(get_lowest_cost_of_decorating_venues(costs)) # Output: 7


if __name__ == "__main__":
    main()