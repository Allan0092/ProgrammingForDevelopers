class Maze:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.potential_locks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'T', 'U', 'V', 'X', 'Y', 'Z']
        self.potential_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        self.keys: list[str] = self.get_all_hidden_keys()
        self.found_keys = []
        self.locks = []
        self.deadEnds = []
        self.visited: list[int, int] = []
        self.start: list[int, int] = self.find_starting_position()
        self.current: list[int, int] = self.start.copy()

    def find_starting_position(self) -> list[int, int]:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'S':
                    return [i, j]

    def game_over(self) -> bool:
        if set(self.keys) == set(self.found_keys): # all keys have been found
            return True
        return False

    def get_all_hidden_keys(self):
        keys = []
        for floor in self.grid:
            for value in floor:
                if value in self.potential_keys:
                    keys.append(value)
        return keys

    def depth_first_search(self, target: str) -> list[int, int]:
        visited: list[int, int] = []
        self.found_keys = []
        def dft(curr: list[int, int]):
            if curr in visited or self.grid[curr[0]][curr[1]] == 'W': # if visited or a wall
                return
            # The key for the lock is not found.
            if self.grid[curr[0]][curr[1]] in self.potential_locks and self.grid[curr[0]][curr[1]].lower() not in self.found_keys:
                return 
            visited.append(curr)
            if self.grid[curr[0]][curr[1]] in self.keys: # Adds the found key.
                self.found_keys.append(self.grid[curr[0]][curr[1]])
            # Directions to treverse.
            if curr[0]>0: # Up
                dft([curr[0]-1, curr[1]])
            if curr[1]<len(self.grid[curr[0]])-1: # Right
                dft([curr[0], curr[1]+1])
            if curr[0]<len(self.grid)-1: # Down
                dft([curr[0]+1, curr[1]])
            if curr[1]>0: # Left
                dft([curr[0], curr[1]-1])
        dft(self.start)
        return visited

    def breadth_first_triversal(self):
        visited: list[list[int, int]] = []
        self.found_keys:list[self.potential_keys] = []
        move: int = 0
        maze_queue: list[list[int, int]] = [[self.start, move]]
        collected_keys: list[str] = []
        while len(maze_queue)>0:
            curr, move = maze_queue.pop(0)
            curr_value: str = self.grid[curr[0]][curr[1]]
            if len(self.keys) == len(collected_keys): # all keys collected
                self.found_keys = collected_keys
                break
            if curr in visited or curr_value == "W": # already visited or a wall
                continue
            if curr_value in self.potential_locks:# if in a lock
                if curr_value.lower() not in collected_keys: # if key not found
                    continue
            visited.append(curr)
            if curr_value in self.potential_keys:
                collected_keys.append(curr_value)
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


    def can_move(self, current:list[int, int], destination: list[int, int]) -> bool:
        destination_value: str = self.grid[destination[0]][destination[1]] # get the value of the current path.
        if destination_value == "P": # if there is a path
            return True
        if destination_value == 'W': # if there is a wall
            return False
        if destination_value in self.locks and destination_value.lower() in self.collected_keys: # if the lock's key is collected.
            return True
        return False


def main():
    grid = [
        ["S", "P", "q", "P", "P"],
        ["W", "W", "W", "P", "W"],
        ["r", "P", "Q", "p", "R"]
    ]

    game = Maze(grid)
    print(game.start)
    print(game.keys)
    # print(game.depth_first_search(-1))
    print(game.breadth_first_triversal())


if __name__ == "__main__":
    main()