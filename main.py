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

    num_particles = 100
    max_iter = 500
    #cs = [1, 2, 3]
    cs = [0, 0.25, 0.5, 0.75, 1]
    ws = [0.1,0.2, 0.3, 0.4, 0.5, 0.6]

    for c1 in cs:
        for c2 in cs:
            for w in ws:
                if not (c1 == 0 and c2 == 0):
                    best_coloring, best_fitness = PSO(G, num_colors, G.number_of_edges(), num_particles, max_iter, w, c1, c2)
                    print("##########################################################################")
                    print(f"Parâmetros: c1 = {c1}, c2 = {c2}, w = {w}")
                    #print("Melhor coloração encontrada:", best_coloring)
                    print(f"Best fitness: {best_fitness}")
                    
                    print([int(round(pos)) for pos in best_coloring])
                    print("##########################################################################")
                    #save_colored_graph(G, best_coloring,"graph.png")