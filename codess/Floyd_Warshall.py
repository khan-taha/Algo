import networkx as nx


def main_Floyd_Warshall(filename):
    DG = nx.DiGraph()

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

    def Floyd_Warshall():  # DP table
        for k in range(rows):
            for i in range(rows):
                for j in range(cols):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    file(filename)

    rows = DG.number_of_nodes()
    cols = DG.number_of_nodes()
    rows, cols = (rows, cols)
    cost = [[100.0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        cost[i][i] = 0

    for (i, j) in DG.edges():
        cost[i][j] = DG[i][j]['weight']
        # cost[j][i] = DG[i][j]['weight'] #uncomment for undirected

    Floyd_Warshall()
    total_cost = 0.0
    inf = False

    for i in range(rows):
        for j in range(cols):
            print("({},{}) = {} ".format(i, j, cost[i][j]), end=" ")
            if cost[i][j] == 100.0:
                inf = True
            else:
                total_cost = total_cost + cost[i][j]
        print("")
    if inf:
        print("total cost = {} + INFINITY".format(total_cost))
    else:
        print("total cost = {} ".format(total_cost))
