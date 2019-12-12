import networkx as nx
import matplotlib.pyplot as plt


def main_Prims(filename):
    DG = nx.Graph()
    G1 = nx.Graph()
    source_edge = (0, 0)

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
            cords.append((x[1], x[2]))

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

    # print(DG.edges(data=True))
    def findmin(visited):
        m = 999999
        x = 0
        y = 0

        for (i, j) in DG.edges():
            if visited[i] or visited[j]:

                if DG[i][j]['weight'] < float(m) and not (visited[j] and visited[i]):
                    m = DG[i][j]['weight']
                    x = int(i)
                    y = int(j)

        visited[y] = True
        visited[x] = True
        return x, y

    def prims(e1, e2):
        x = 0,
        y = 0
        V = DG.number_of_nodes()

        visited = [False] * DG.number_of_nodes()
        visited[e1] = True
        visited[e2] = True
        G1.add_node(int(e1), pos=(cords[int(e1)][0], cords[int(e1)][1]))
        G1.add_node(int(e2),
                    pos=(cords[int(e2)][0], cords[int(e2)][1]))  # adding the min cost edge to G1 to create the MST
        G1.add_edge(int(e1), int(e2), weight=DG[int(e1)][int(e2)]['weight'])
        DG.remove_edge(int(e1), int(e2))  # deleting that edge from the original graph
        edges = 1

        while edges < V - 1:
            (x, y) = findmin(visited)  # getting the next minimum cost vertex
            G1.add_node(int(x), pos=(cords[int(x)][0], cords[int(x)][1]))
            G1.add_node(int(y), pos=(cords[int(y)][0], cords[int(y)][1]))
            if x != y:
                G1.add_edge(int(x), int(y), weight=DG[int(x)][int(y)]['weight'])
                DG.remove_edge(int(x), int(y))
            edges += 1

        return G1

    cords = file(filename)

    Min = 999999
    for (i, j) in DG.edges():
        if DG[i][j]['weight'] < Min:
            source_edge = (i, j)
            Min = DG[i][j]['weight']
    # print("graph vertices {}".format(DG.number_of_nodes()))
    G1 = prims(source_edge[0], source_edge[1])  # starting with the minimum cost edge
    # print("MST edges {}".format(G1.number_of_edges()))

    print(G1.edges(data=True))

    cost = 0
    for (i, j) in G1.edges():
        cost = cost + G1[i][j]['weight']
    print("total cost = {}".format(cost))
    printgraph(G1)
