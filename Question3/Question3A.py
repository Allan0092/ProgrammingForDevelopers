"""
for the given problem, 
let us initialize an empty list to store called self.stream

in the getMedian,
    First sort the list of scores.
    We can send the middle number of the sorted list if the list is odd.
    We can calculate the average of the two middle numbers of the sorted list.

"""


class ScoreTracker:
    def __init__(self):
        """Initialize an empty list for storing the scores from different assignments.
        """
        self.stream = [] # initialize a new empty list
    
    def addScore(self, score: float) -> None:
        """adds a new score to the stream

        Args:
            score (float): score of the assignment
        """
        self.stream.append(score) # appends the score to the stream
    
    def getMedianScore(self) -> float:
        """calculates the median of the score stream

        Returns:
            float: median score
        """
        if len(self.stream)==0: # returns 0 if no scores are given.
            return 0
        sorted_stream = sorted(self.stream) # sorts the scores in the stream.
        if len(sorted_stream)%2==0: # if the number of scores in the stream is even
            middle_index = len(sorted_stream)//2 # finds the middle of the index
            num1 = sorted_stream[middle_index-1] # gets the first middle number in the score stream.
            num2 = sorted_stream[middle_index] # gets the secound middle number in the score stream.
            return (num1 + num2)/2 # gets the average of the two middle numbers on the score stream
        else: # if the number of scores in the stream is odd
            return sorted_stream[(len(sorted_stream)//2)] # returns the middle number in the sorted stream of scores


def main():
    scoreTracker = ScoreTracker()
    scoreTracker.addScore(85.5) # Stream: [85.5]
    scoreTracker.addScore(92.3) # Stream: [85.5, 92.3]
    scoreTracker.addScore(77.8) # Stream: [85.5, 92.3, 77.8]
    scoreTracker.addScore(90.1) # Stream: [85.5, 92.3, 77.8, 90.1]
    median1 = scoreTracker.getMedianScore() # Output: 87.8 (average of 90.1 and 85.5)

    scoreTracker.addScore(81.2) # Stream: [85.5, 92.3, 77.8, 90.1, 81.2]
    scoreTracker.addScore(88.7) # Stream: [85.5, 92.3, 77.8, 90.1, 81.2, 88.7]
    median2 = scoreTracker.getMedianScore() # Output: 87.1 (average of 88.7 and 85.5)

    print(f"median1: {median1}\nmedian2: {median2}")

    scoreTracker2 = ScoreTracker()
    for i in [0, 1,2,3,4, 5, 6, 7, 8]:
        scoreTracker2.addScore(i)
    print(f"median4: {scoreTracker2.getMedianScore()}") # Output: 4


if __name__ == "__main__":
    main()