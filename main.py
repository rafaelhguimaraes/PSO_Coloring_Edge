import networkx as nx
from pso import *

def read_graph_from_col_file(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            nodes = list(map(int, line.strip().split()))
            G.add_edge(nodes[0], nodes[1])
    return G

def save_colored_graph(graph, coloring, filename):
    pos = nx.spring_layout(graph)  # posicao dos nos
    colors = [int(round(pos)) for pos in coloring]
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', edge_color=colors, width=2, 
        edge_cmap=plt.cm.viridis, vmin=0, vmax=max(coloring))
    plt.savefig(filename)

if __name__ == "__main__":
    grafo = "Testes/myciel4.col"
    G = read_graph_from_col_file(grafo)
    num_colors = max(dict(G.degree()).values())

    num_particles = [300, 400, 500, 750, 1000]
    max_iters = [750, 1000, 1500, 2000, 3000]
    c = 2
    w = 0.4

    for num_particle in num_particles:
        for max_iter in max_iters:
            best_coloring, best_fitness = PSO(G, num_colors, G.number_of_edges(), num_particle, max_iter, w, c, c)
            print("##########################################################################")
            print(f"Parâmetros: num_particless = {num_particle}, max_iters = {max_iter}")
            #print("Melhor coloração encontrada:", best_coloring)
            print(f"Best fitness: {best_fitness}")
            
            print([int(round(pos)) for pos in best_coloring])
            print("##########################################################################")
            #save_colored_graph(G, best_coloring,"graph.png")