import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from particle import *

def num_conflicts(graph:nx.Graph(), num_colors, num_edges, colors):
    violations = 0
    edges = list(graph.edges())
    edges_colors = []

    for i in range(num_edges):
        edges_colors.append([edges[i][0], edges[i][1], colors[i]])

    num_vertices = graph.number_of_nodes() 
    for v in range(1, num_vertices+1):
        b = [0] * (num_colors + 2)
        for x in edges_colors:
            if x[0] == v or x[1] == v:
                if b[x[2]] == 0:
                    b[x[2]] = 1
                else:
                    violations += 1
    return violations

def fitness(graph, positions, num_colors, num_edges):
    colors = [int(round(pos)) for pos in positions]

    conflicts = num_conflicts(graph, num_colors, num_edges, colors)
    
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

def PSO(graph, num_colors, num_edges, num_particles, max_iter):
    particles = [Particle(graph.number_of_edges(), num_colors) for _ in range(num_particles)]
    global_best_position = None
    global_best_fitness = float('inf')

    for iter in range(max_iter):
        for particle in particles:
            fitness_value = fitness(graph, particle.position, num_colors, num_edges)
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