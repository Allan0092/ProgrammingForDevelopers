""" 
Using breath first search, we can get the shortest path,
along with adding the constraints of the game.

"""

class Maze:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.potential_locks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'T', 'U', 'V', 'X', 'Y', 'Z']
        self.potential_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        self.keys: list[str] = self.get_all_hidden_keys() # All the hidden keys of the game
        self.found_keys = []
        self.locks = []
        self.visited: list[int, int] = []
        self.start: list[int, int] = self.find_starting_position()

    def find_starting_position(self) -> list[int, int]:
        """Finds the starting position in the maze

        Returns:
            list[int, int]: the starting postion in the maze
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'S':
                    return [i, j]

    def get_all_hidden_keys(self) -> list[str]:
        """Get all the hidden keys in the maze

        Returns:
            list[str]: list of keys
        """
        keys = []
        for floor in self.grid:
            for value in floor:
                if value in self.potential_keys:
                    keys.append(value)
        return keys

    def breadth_first_triversal(self):
        """Using Breadth first triversal, travel through each path in the maze in a Queue

        Returns:
            int: minimum number of moves | if impossible : -1
        """
        visited: list[list[int, int]] = []
        self.found_keys:list[self.potential_keys] = []
        move: int = 0
        maze_queue: list[list[int, int]] = [[self.start, move]]
        collected_keys: list[str] = []
        while len(maze_queue)>0:
            curr, move = maze_queue.pop(0)
            curr_value: str = self.grid[curr[0]][curr[1]]
            if curr_value in self.potential_keys:
                collected_keys.append(curr_value)
            if len(self.keys) == len(collected_keys): # all keys collected
                self.found_keys = collected_keys
                return move
            if curr in visited or curr_value == "W": # already visited or a wall
                continue
            if curr_value in self.potential_locks:# if in a lock
                if curr_value.lower() not in collected_keys: # if key not found
                    continue
            visited.append(curr)
            # Directions to treverse.
            if curr[0]>0 and [curr[0]-1, curr[1]] not in visited: # Up
                maze_queue.append([[curr[0]-1, curr[1]], move+1])
            if curr[1]<len(self.grid[curr[0]])-1 and [curr[0], curr[1]+1] not in visited: # Right
                maze_queue.append([[curr[0], curr[1]+1], move+1])
            if curr[0]<len(self.grid)-1 and [curr[0]+1, curr[1]] not in visited: # Down
                maze_queue.append([[curr[0]+1, curr[1]], move+1])
            if curr[1]>0 and [curr[0], curr[1]-1] not in visited: # Left
                maze_queue.append([[curr[0], curr[1]-1], move+1])
        
        if len(self.keys) != len(collected_keys): # if all the keys cannot be found.
            return -1
        return move

def main():
    # Given input
    grid = [
        ["S", "P", "q", "P", "P"],
        ["W", "W", "W", "P", "W"],
        ["r", "P", "Q", "p", "R"]
    ]

    game = Maze(grid)
    print(f"Stating Position: {game.start}") # FInds out the starting position
    print(f"All Keys: {game.keys}") # Finds out all the keys
    print(game.breadth_first_triversal()) # output: 8


if __name__ == "__main__":
    main()