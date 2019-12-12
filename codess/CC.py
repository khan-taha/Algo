import networkx as nx
import statistics


def main_CC(filename):
    DG = nx.Graph()

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

    file(filename)

    V = DG.nodes()
    E = DG.edges()

    neighbours = [0] * DG.number_of_nodes()

    Nv = 0
    CC = [0] * DG.number_of_nodes()
    kv = 0
    index = 0

    for i in V:

        for (j, k) in E:

            if j == i:
                neighbours[k] = 1
            # Nv is the the number of connections b/w the neighbours of a vertex
            elif k == i:
                neighbours[j] = 1
        for (m, n) in E:  # checking connection bw neighbours
            if (neighbours[m] and neighbours[n]) and m != i and n != i:
                Nv += 1
        var = (DG.degree[i]) * (DG.degree[i] - 1)
        if var != 0:
            CC[index] = (2 * Nv) / var
        else:
            CC[index] = 0
        index += 1
        Nv = 0
        neighbours = [0] * DG.number_of_nodes()

    print(statistics.mean(CC))
