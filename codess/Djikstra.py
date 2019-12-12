import networkx as nx
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


def main_Dijkstra(filename):
    DG = nx.Graph()

    def printgraph(A):
        plt.close()
        vertex = nx.get_node_attributes(A, 'pos')
        plt.figure(3, figsize=(25, 25), dpi=80)
        nx.draw(A, vertex, node_color='r', with_labels=True)
        labels = nx.get_edge_attributes(A, 'weight')
        nx.draw_networkx_edge_labels(A, vertex, edge_labels=labels)

        plt.show()

    def file(filename):
        index = 0

        f = open(filename, "r")

        f.readline()
        while 1:
            s = f.readline()
            if s.isspace():
                continue
            x = s.split()
            break
        x = list(map(float, x))

        f.readline()

        for i in range(int(x[0])):
            s = f.readline()
            x = s.split()
            x = list(map(float, x))
            DG.add_node(int(x[0]), pos=(x[1], x[2]))

        f.readline()
        while 1:
            s = f.readline()
            if s.isspace():
                break
            x = s.split()
            x = list(map(float, x))
            while index + 1 < len(x):
                if x[0] == x[index + 1]:
                    index += 4
                    continue
                if DG.has_edge(int(x[0]), int(x[index + 1])):

                    DG[int(x[0])][int(x[index + 1])]['weight'] = min(DG[int(x[0])][int(x[index + 1])]['weight'],
                                                                     x[index + 3] / 10000000)
                else:
                    DG.add_edge(int(x[0]), int(x[index + 1]), weight=x[index + 3] / 10000000)
                # print((int(x[0]), int(x[index + 1]), DG[int(x[0])][int(x[index + 1])]['weight']))
                index += 4
            index = 0
        s = f.readline()
        source_node = s.split()
        source_node = int((list(map(float, source_node)))[0])

        return source_node

    def inedge(u, v):
        edges = DG.edges()
        for i in edges:
            if (u, v) == i or (v, u) == i:  # uncomment for undirected
                return True
        return False

    def findmin():  # finding the vertex with the minimum distance
        Min = 1000.00
        index = 0

        for i, d in enumerate(distance):

            if d < Min and not visited[i]:
                Min = d
                index = i
        return index

    def Dijkstra():
        v = 0
        while len(Vertices) > 0:
            v = findmin()
            visited[v] = 1
            Vertices.remove(v)
            for i in Vertices:

                if inedge(v, i):

                    if (DG[v][i]['weight'] + distance[v] < distance[i]) and not visited[i]:
                        distance[i] = DG[v][i]['weight'] + distance[v]

    source_node = file(filename)

    distance = [100.00] * DG.number_of_nodes()
    distance[source_node] = 0
    visited = [0] * DG.number_of_nodes()
    Vertices = DG.nodes()
    Vertices = list(Vertices)

    Dijkstra()
    total_cost = 0.0
    inf = False
    # print(nx.dijkstra_path_length(DG, 1, 3))
    for i, d in enumerate(distance):
        print("distance from {} to {} is {}".format(source_node, i, d))
        if d == 100.0:
            inf = True
        total_cost = total_cost + d

    if inf:
        print("Total cost = INFINITY")
    else:
        print("Total cost = {}".format(total_cost))

    mapping = {}
    keys = range(DG.number_of_nodes())

    for i in keys:  # this changes the label of the vertex to cost
        mapping[i] = distance[i]
    DG = nx.relabel_nodes(DG, mapping)
    printgraph(DG)
