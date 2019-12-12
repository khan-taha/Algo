import networkx as nx
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename


def main_Kruskal(filename):
    DG = nx.Graph()  # creating an undriected graph
    G1 = nx.Graph()  # undriected graph to show the MST output

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
        cords = [] * DG.number_of_nodes()
        for i in range(int(x[0])):
            s = f.readline()
            x = s.split()
            x = list(map(float, x))
            DG.add_node(int(x[0]), pos=(x[1], x[2]))
            G1.add_node(int(x[0]), pos=(x[1], x[2]))

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
        return cords

    def join(x, y):
        parent[x] = parent[y]

    def find_parent(x):  # this function checks the parent of the two vertices of the same edge , if their parents
        # are same then cycle
        if x == parent[x]:
            return x
        else:

            return find_parent(parent[x])

    def Kruskal(edgelist):
        v = (0, 0)
        v1 = 0
        v2 = 0
        index = 0
        V = DG.number_of_nodes()
        edge = 0
        while edge < V - 1:

            v = edgelist[index]

            v1 = find_parent(v[0])
            v2 = find_parent(v[1])

            if v1 != v2:
                G1.add_edge(v[0], v[1], weight=DG[v[0]][v[1]]['weight'])
                join(v1, v2)
                edge += 1
            index += 1

    file(filename)

    edges = sorted(DG.edges(data=True), key=lambda t: t[2].get('weight', 1))  # sorting list according to weights

    edgelist = []
    for i in edges:
        edgelist.append((i[0], i[1]))

    parent = []
    for i in G1.nodes():
        parent.append(i)

    Kruskal(edgelist)
    print(G1.edges(data=True))

    cost = 0
    for (i, j) in G1.edges():
        cost = cost + G1[i][j]['weight']
    print("total cost = {}".format(cost))
    printgraph(G1)
