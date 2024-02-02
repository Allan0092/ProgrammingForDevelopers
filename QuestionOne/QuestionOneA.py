"""
Here,
In an Array of Cost[n][k], [n] = venues and [k] = themes. 


Constraints: 
Cost[n][k]!=Cost[n+1][k] or Cost[n-1][k]. 
Find minimum Cost

"""


def createCostTable(cost):
    sum_table = [[0,0,0],[0,0,0], [0,0,0]]
    for n in range(len(cost[0])):
        for k in range(len(cost[1])):
            if n==k:
                sum_table[n][k]=-1
                continue
            sum_table[n][k]=cost[0][k]+cost[1][n] 

    return sum_table


def main():
    cost=[[1,5,3],[2,9,4]]
    print(createCostTable(cost))
    

if __name__=="__main__":
    main()