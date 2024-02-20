"""
We can solve this problem using sets
First we create a set of individuals that know the secret 

Then we iterate over each time intervals, extracting the start and the end time.
Then create another set of new individuals that knows the secret.
Then assign the set of individuals who know the secret by taking the union of the new individuals and the new individuals.
"""

def eventually_known_individuals(n, intervals, firstperson):
    known_individuals = set() # initialize an emply set of known individuals
    known_individuals.add(firstperson)  # the firstperson that knows the secret.

    for start, end in intervals: # Update the set of known individuals during the current time interval
        new_individuals = set(range(start, end + 1)) # get the set of new individuals
        known_individuals |= new_individuals # get the union of teh known individual and the new individuals and assign it to known individuals
    return list(known_individuals) # cast the set as a list and return it.


def main():
    # Given inputs
    n = 5
    intervals = [(0, 2), (1, 3), (2, 4)]
    first_person = 0

    result: list[int] = eventually_known_individuals(n, intervals,first_person)
    print(result) # Output: [0, 1, 2, 3, 4]


if __name__ == "__main__":
    main()