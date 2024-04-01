import random

class Particle:
    def __init__(self, num_edges, num_colors):
        #self.position = [random.uniform(1, num_colors) for _ in range(num_edges)]
        self.position = [1+random.random()*(num_colors-1) for _ in range(num_edges)]
        self.velocity = [random.uniform(-1, 1) for _ in range(num_edges)]
        self.best_position = self.position[:]
        self.best_fitness = float('inf')
        self.num_edges = num_edges
        self.num_colors = num_colors