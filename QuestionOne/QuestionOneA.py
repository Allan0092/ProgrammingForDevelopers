"""
Here,
In an Array of Cost[n][k], [n] = venues and [k] = themes. 


Constraints: 
Cost[n][k]!=Cost[n+1][k] or Cost[n-1][k]. 
Find minimum Cost

Solution:

Step 1:
For a list of costs[n][k], 
A list of sum_table[len(n)][len(k)] is created with all possible sum of costs.
The same index of costs[0][k] and costs[1][k] is -1.(constraint)
The index of previously chosen theme is also -1.(adjacency constraint.)

So, for costs = [[1,5,3], [2, 9, 4]]
sum_table = [[-1,  10,  5], 
             [ 7,  -1,  9], 
             [ 5,  12, -1]]
This is achieved by using the createCostTable function.

Step 2:
For the given cost input, make sure that a sum_table is created for a couple,
then find the minimum value from the sum_table along with it's index.
This is done using the findMin function.

Step 3:
Manage the input costs list in such a way that only two nested lists are send at a time to Step 1,
and remember all the chosen theme's indexes for all the venue to avoid choosing it again for the 
adjacent venue.
Keep adding the minimum values for each sum_table.
At last if a single odd list is left, find the minimum value in the list and add it as well.
This is done using the calculateDecorationCost function.
"""

import sys

def createCostTable(costs, prev_choosen = []):
    '''
        This function creates a [k][k] length of list of the sum of two theme of two venues. The value for the same theme is -1.
            Parameters:
                costs (int[n:Venue][k:theme]): cost of decorating the venue.
                prev_choosen (int) : previous index of the choosen theme, which cannot be choosen again.
        
            Returns:
                int[k][k] : sum of all the possible cost between two venues.
    '''
    if prev_choosen==[]:# for the first two list of the input.
        prev_choosen=-1
    else:# when there is a value for the previously chosen index.
        prev_choosen=prev_choosen[-1]
    sum_table = []
    for i in range(len(costs[0])): # For creating an empty list of sum_table of length [first venue] [second venue]
        sum_table.append([])
        for j in range(len(costs[1])):
            sum_table[i].append(None) # assigns None.
    
    for i in range(len(costs[0])):
        for j in range(len(costs[1])):
            if i==j or i == prev_choosen:# if the theme of both the venue is same or already choosen by the previous venue.
                sum_table[i][j]=-1
                continue
            sum_table[i][j]=costs[0][i]+costs[1][j] # adds the cost of corresponding themes of both venues.
    return sum_table


def findMin(sum_table) -> (int, [int, int]):
    '''
        Finds the minimum value in the nested array
            Parameters:


            Returns:
                int : smallest int
                int[] : index of the smallest int
    '''
    chosen_index = [-1,-1] # in the form of [0,1] meaning in the index 1 of the nested index 0 array.
    least_cost = sys.maxsize # the maximum value of an int
    a = [-1]*(len(sum_table)*len(sum_table[0])) # create a list of length of all the values from the sum_table list
    for i in range(len(sum_table)):# Iterating over the venues
        for j in range(len(sum_table[i])):# Iterating over the cost of themes
            if sum_table[i][j]<least_cost and sum_table[i][j]!=-1: # for getting the minimum cost and validating adjacency constraint.
                least_cost=sum_table[i][j]
                chosen_index=[i,j]
    return least_cost, chosen_index

def calculateDecorationCost(costs):
    '''
    
    '''
    if len(costs)==1:
        return min(costs)
    costs_length = len(costs) # the number of venues given
    i = 0 # for slicing the venues
    chosen_indexes = [] # the list of chosen minimum indexes.
    minimum_cost = 0 # the minimum cost of decorating the venues.
    while(costs_length>1): # until only one or none of the venues are left.
        sum_table = createCostTable(costs[i:i+2], chosen_indexes)
        findMin_output=findMin(sum_table)
        minimum_cost += findMin_output[0]
        chosen_indexes.extend(findMin_output[1])
        costs_length-=2
        i+=2
    if costs_length==1: # when a venue is still left 
        costs[-1][chosen_indexes[-1]]=sys.maxsize # Assigns the maximum value an int can have.
        minimum_cost+=min(costs[-1])
    return minimum_cost



def main():
    costs=[[1,5,3], [2, 9, 4]]
    print(calculateDecorationCost(costs)) # 5
    
    costs = [[1,3,2], [4,6,8], [3,1,5]] 
    print(calculateDecorationCost(costs)) # 7

    costs = [[1,3,2], [4,6,8], [3,1,5], [11,1,1], [11,1212,412,55,66]]
    print(calculateDecorationCost(costs)) # 19


if __name__=="__main__":
    main()