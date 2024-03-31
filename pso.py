import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, num_edges, num_colors):
        self.position = [random.uniform(1, num_colors) for _ in range(num_edges)]
        self.velocity = [random.uniform(-1, 1) for _ in range(num_edges)]
        self.best_position = self.position[:]
        self.best_fitness = float('inf')

def fitness(graph, positions, num_colors):
    colors = [int(round(pos)) for pos in positions]
    conflicts = 0
    for u, v in graph.edges():
        if colors[u] == colors[v]:
            conflicts += 1
    penalty = conflicts ** 2  # Aumenta a penalidade quadraticamente com o número de conflitos
    return conflicts + penalty


def update_velocity(particle, global_best_position, inertia_weight, cognitive_weight, social_weight):
    for i in range(len(particle.velocity)):
        cognitive_component = random.random() * cognitive_weight * (particle.best_position[i] - particle.position[i])
        social_component = random.random() * social_weight * (global_best_position[i] - particle.position[i])
        particle.velocity[i] = inertia_weight * particle.velocity[i] + cognitive_component + social_component

def update_position(particle, num_colors):
    for i in range(len(particle.position)):
        new_position = particle.position[i] + particle.velocity[i]
        particle.position[i] = max(1, min(num_colors, new_position))

def PSO(graph, num_colors, num_particles, max_iter):
    particles = [Particle(graph.number_of_edges(), num_colors) for _ in range(num_particles)]
    global_best_position = None
    global_best_fitness = float('inf')

    for iter in range(max_iter):
        for particle in particles:
            fitness_value = fitness(graph, particle.position, num_colors)
            if fitness_value < particle.best_fitness:
                particle.best_fitness = fitness_value
                particle.best_position = particle.position[:]
            if fitness_value < global_best_fitness:
                global_best_fitness = fitness_value
                global_best_position = particle.position[:]
        
        print(f"Iteração {iter + 1}: Melhor fitness = {global_best_fitness}")

        for particle in particles:
            update_velocity(particle, global_best_position, 1, 2, 2)
            update_position(particle, num_colors)

    return global_best_position 

def plot_colored_graph(graph, coloring):
    pos = nx.spring_layout(graph)  # posicao dos nos
    colors = [int(round(pos)) for pos in coloring]
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', edge_color=colors, width=2, 
        edge_cmap=plt.cm.viridis, vmin=0, vmax=max(coloring))
    plt.show()

# Exemplo de utilização
if __name__ == "__main__":
    # Criando um grafo de exemplo
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

    # Definindo parâmetros
    num_colors = 3
    num_particles = 10
    max_iter = 100

    # Executando PSO
    best_coloring = PSO(G, num_colors, num_particles, max_iter)
    print("Melhor coloração encontrada:", best_coloring)

    # Mostrando o grafo colorido
    plot_colored_graph(G, best_coloring)
