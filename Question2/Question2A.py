"""
For this problem we can first calculate the following values:
total number of dresses,
total number of super sewing machines
the average number of dresses

Then the best case can be if the total number of dresses divided by 
the total number of sewing machines gives a remainder, then return -1 to
denote that the clothes cannot be distributed equally.

Then we can iterate over the number of dresses in each machine.
While iterating we can increment the balance by the difference of dresses and 
the average of dresses to get the number of dresses missing in that machine.

Then we can add the number of moves by comparing the current moves with the 
value of balance and assign the maximum between them.
"""


def min_moves_to_equalize_dresses(sewing_machines):
    total_dresses = sum(sewing_machines) # get the total number of dresses.
    num_machines = len(sewing_machines) # get the total number of machines.
    average_dresses = total_dresses // num_machines # get the average number of dresses.

    if total_dresses % num_machines != 0:
        return -1  # Cannot equalize the number of dresses.
    moves = balance = 0 # initialize the number of moves and balance.
    for dresses in sewing_machines: # iterate over each dress in the sewing machine.
        balance += dresses - average_dresses # find the number of clothes needed to balance the clothes in the sewing machine.
        moves = max(moves, abs(balance)) # compare between the moves and the clothes needed to balance.
    return moves # return the minimum number of moves.


def main():
    sewing_machines = [1, 0, 5] # given input
    print(min_moves_to_equalize_dresses(sewing_machines))  # Output: 3


if __name__ == "__main__":
    main()