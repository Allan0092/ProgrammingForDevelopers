import numpy as np # for matrix
import random 

class AntColony:
    def __init__(self, distance_matrix, num_ants, num_iterations, decay_factor=0.5, alpha=1, beta=2, evaporation_rate=0.5):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay_factor = decay_factor
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.pheromone_matrix = np.ones((self.num_cities, self.num_cities))
        self.best_path = None
        self.best_path_length = float('inf')

    def run(self):
        for _ in range(self.num_iterations):
            self._run_single_iteration()
            self._update_pheromones()
            if self.best_path_length < float('inf'):
                print(f"Best path length after iteration {_+1}: {self.best_path_length}")
                print(f"Best path: {self.best_path}")

    def _run_single_iteration(self):
        self.ants = [Ant(self) for _ in range(self.num_ants)]
        for ant in self.ants:
            ant.construct_solution()
            if ant.path_length < self.best_path_length:
                self.best_path_length = ant.path_length
                self.best_path = ant.path

    def _update_pheromones(self):
        self.pheromone_matrix *= (1 - self.evaporation_rate)
        for ant in self.ants:
            for i in range(len(ant.path) - 1):
                self.pheromone_matrix[ant.path[i], ant.path[i+1]] += 1 / ant.path_length
                self.pheromone_matrix[ant.path[i+1], ant.path[i]] += 1 / ant.path_length

class Ant:
    def __init__(self, ant_colony):
        self.ant_colony = ant_colony
        self.visited = [False] * self.ant_colony.num_cities
        self.path = []
        self.path_length = float('inf')

    def construct_solution(self):
        start_city = random.randint(0, self.ant_colony.num_cities - 1)
        self.path = [start_city]
        self.visited[start_city] = True
        for _ in range(self.ant_colony.num_cities - 1):
            next_city = self._select_next_city()
            self.path.append(next_city)
            self.visited[next_city] = True
        self.path.append(start_city)
        self.path_length = self._calculate_path_length()

    def _select_next_city(self):
        current_city = self.path[-1]
        unvisited_cities = [i for i in range(self.ant_colony.num_cities) if not self.visited[i]]
        probabilities = [self.ant_colony.pheromone_matrix[current_city, next_city]**self.ant_colony.alpha /
                         (self.ant_colony.distance_matrix[current_city, next_city]**self.ant_colony.beta) for next_city in unvisited_cities]
        probabilities /= np.sum(probabilities)
        next_city = np.random.choice(unvisited_cities, p=probabilities)
        return next_city

    def _calculate_path_length(self):
        length = 0
        for i in range(len(self.path) - 1):
            length += self.ant_colony.distance_matrix[self.path[i], self.path[i+1]]
        return length

def main():
    distance_matrix = np.array([
        [0, 2, 3, 4],
        [2, 0, 6, 1],
        [3, 6, 0, 2],
        [4, 1, 2, 0]
    ])
    num_ants=10
    num_iterations=100
    ant_colony=AntColony(distance_matrix, num_ants, num_iterations)
    ant_colony.run()


if __name__ == "__main__":
    main()


