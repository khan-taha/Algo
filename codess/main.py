from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import networkx as nx
from CC import *
from Bellman_Ford import *
from Djikstra import *
from Floyd_Warshall import *
from prims import *
from kruskal import *

filename = ""
DG = nx.DiGraph()


def printgraph(A):
    vertex = nx.get_node_attributes(A, 'pos')
    plt.figure(3, figsize=(25, 25), dpi=80)
    nx.draw(A, vertex, node_color='r', with_labels=True)
    labels = nx.get_edge_attributes(A, 'weight')
    nx.draw_networkx_edge_labels(A, vertex, edge_labels=labels)
    plt.show()


def file(f):  # this function is to set up our graph by reading the given file
    index = 0

    f.readline()
    while 1:
        s = f.readline()
        if s.isspace():  # ignore the whitespaces
            continue
        x = s.split()
        break
    x = list(map(float, x))  # coverting the readline into a list of floats

    f.readline()

    for i in range(int(x[0])):
        s = f.readline()
        x = s.split()
        x = list(map(float, x))
        DG.add_node(int(x[0]), pos=(x[1], x[2]))  # adding node to graph

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
            #considering the minimum cost edge if there are more than one path b/w two vertices
                DG[int(x[0])][int(x[index + 1])]['weight'] = min(DG[int(x[0])][int(x[index + 1])]['weight'], 
                                                                 x[index + 3] / 10000000)
            else:
                DG.add_edge(int(x[0]), int(x[index + 1]), weight=x[index + 3] / 10000000)
            # print((int(x[0]), int(x[index + 1]), DG[int(x[0])][int(x[index + 1])]['weight']))
            index += 4
        index = 0
    printgraph(DG)


def Prims():
    main_Prims(filename)


def Kruskal():
    main_Kruskal(filename)


def Dijkstra():
    main_Dijkstra(filename)


def Bellman_Ford():
    main_Belman_Ford(filename)


def Floyd_Warshall():
    main_Floyd_Warshall(filename)


def CC():
    main_CC(filename)


def clicked():
    global window
    global root
    if window is not None:
        window.destroy()
    global filename
    filename = askopenfilename(filetypes=[("Text file", "*.txt")])
    f = open(filename, "r")
    root = Tk()
    root.title("Run your desired Graph Algorithms !!")

    button_frame = Frame(root)
    button_frame.pack(fill=X, side=BOTTOM)

    btn1 = Button(button_frame, text="Prim's", command=Prims)
    btn2 = Button(button_frame, text="Kruskal", command=Kruskal)
    btn3 = Button(button_frame, text="Dijkstra", command=Dijkstra)
    btn4 = Button(button_frame, text="Bellman Ford", command=Bellman_Ford)
    btn5 = Button(button_frame, text="Floyd Warshall Algorithm", command=Floyd_Warshall)
    btn6 = Button(button_frame, text="Clustering Coefficient", command=CC)
    btn7 = Button(button_frame, text="Select other input file", command=main_window)
    btn8 = Button(button_frame, text="exit", command=root.destroy)

    button_frame.columnconfigure(0, weight=1)
    button_frame.rowconfigure(0, weight=1)

    btn1.grid(row=0, column=0, sticky=W + E + N + S)
    btn2.grid(row=1, column=0, sticky=W + E + N + S)
    btn3.grid(row=2, column=0, sticky=W + E + N + S)
    btn4.grid(row=3, column=0, sticky=W + E + N + S)
    btn5.grid(row=4, column=0, sticky=W + E + N + S)
    btn6.grid(row=5, column=0, sticky=W + E + N + S)
    btn7.grid(row=6, column=0, sticky=W + E + N + S)
    btn8.grid(row=7, column=0, sticky=W + E + N + S)
    file(f)
    root.mainloop()


def main_window():
    global window
    global root
    if root is not None:
        root.destroy()
    window = Tk()
    window.title("Select inputfile")
    window.geometry('250x250')
    window.configure(background='black')
    btn = Button(window, text="Select file", command=clicked, bg="blue", activeforeground="red",
                 activebackground="blue")
    btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    window.mainloop()


window = None
root = None

main_window()
