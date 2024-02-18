class Maze:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.potential_locks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
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
        def dft(curr: list[int, int]):
            if curr in visited or self.grid[curr[0]][curr[1]] == 'W': # if visited or a wall
                return
            visited.append(curr)
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
    print(game.depth_first_search(-1))


if __name__ == "__main__":
    main()