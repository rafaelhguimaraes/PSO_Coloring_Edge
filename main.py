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
    grafo = "Testes/myciel3.col"
    G = read_graph_from_col_file(grafo)

    # Definindo parâmetros
    num_colors = 3
    num_particles = 100
    max_iter = 1000


    # Executando PSO
    best_coloring = PSO(G, num_colors, G.number_of_edges(), num_particles, max_iter)
    print("Melhor coloração encontrada:", best_coloring)

    save_colored_graph(G, best_coloring,"graph.png")