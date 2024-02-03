"""
Here,
In an Array of Cost[n][k], [n] = venues and [k] = themes. 


Constraints: 
Cost[n][k]!=Cost[n+1][k] or Cost[n-1][k]. 
Find minimum Cost

"""


def createCostTable(costs):
    '''
        This function creates a [k][k] length of list of the sum of two theme of two venues. The value for the same theme is -1.
            Parameters:
                costs (int[n:Venue][k:theme]): cost of decorating the venue.
        
            Returns:
                int[k][k] : sum of all the possible cost between two venues.
    '''
    # sum_table = [[0,0,0],[0,0,0], [0,0,0]]
    sum_table = []
    for i in range(len(costs[0])):
        sum_table.append([])
        for j in range(len(costs[1])):
            sum_table[i].append(None)
    
    for i in range(len(costs[0])):
        for j in range(len(costs[1])):
            if i==j:
                sum_table[i][j]=-1
                continue
            sum_table[i][j]=costs[0][i]+costs[1][j] 

    return sum_table


def main():
    cost=[[7, 2, 3], [1, 5, 6,7]]
    print(createCostTable(cost))
    

if __name__=="__main__":
    main()