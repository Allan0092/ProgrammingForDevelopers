import sys


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

So, for costs = [[1,5,3], [2, 9, 4]]
sum_table = [[-1,  10,  5], 
             [ 7,  -1,  9], 
             [ 5,  12, -1]]

Step 2:

"""


def createCostTable(costs, prev_choosen = []):
    '''
        This function creates a [k][k] length of list of the sum of two theme of two venues. The value for the same theme is -1.
            Parameters:
                costs (int[n:Venue][k:theme]): cost of decorating the venue.
                prev_choosen (int) : previous index of the choosen theme, which cannot be choosen again.
        
            Returns:
                int[k][k] : sum of all the possible cost between two venues.
    '''
    if prev_choosen==[]:
        prev_choosen=-1
    else:
        prev_choosen=prev_choosen[-1]
    sum_table = []
    for i in range(len(costs[0])):
        sum_table.append([])
        for j in range(len(costs[1])):
            sum_table[i].append(None)
    
    for i in range(len(costs[0])):
        for j in range(len(costs[1])):
            if i==j or i == prev_choosen:
                sum_table[i][j]=-1
                continue
            sum_table[i][j]=costs[0][i]+costs[1][j] 
    return sum_table


def findMin(dp) -> (int, [int, int]):
    '''
        finds the minimum value in the nested array

        Returns:
            int : smallest int
            int[] : index of the smallest int
    '''
    chosen_index = [-1,-1] # in the form of [0,1] meaning in the index 1 of the nested index 0 array.
    least_cost = sys.maxsize # the maximum value of an int
    a = [-1]*(len(dp)*len(dp[0])) # create a list of length of all the values from the dp list
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j]<least_cost and dp[i][j]!=-1:
                least_cost=dp[i][j]
                chosen_index=[i,j]
    return least_cost, chosen_index

def cal(costs):
    costs_length = len(costs)
    i = 0
    chosen_indexes = []
    sum = 0
    while(costs_length>1):
        dp = createCostTable(costs[i:i+2], chosen_indexes)
        findMin_output=findMin(dp)
        sum += findMin_output[0]
        chosen_indexes.extend(findMin_output[1])
        costs_length-=2
        i+=2
    if costs_length==1:
        costs[-1][chosen_indexes[-1]]=sys.maxsize
        sum+=min(costs[-1])
    return sum



def main():
    costs=[[1,5,3], [2, 9, 4]]
    # print(createCostTable(costs))
    # print(findMin(createCostTable(costs)))
    # costs = [[1,3,2], [4,6,8], [3,1,5]]
    print(cal(costs))


if __name__=="__main__":
    main()