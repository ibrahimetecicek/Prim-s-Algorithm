# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:16:57 2021

@author: metec
"""
import numpy as np
from decimal import Decimal
def minimum_spanning_tree(Graph, start_index=-1):
    minimum_spanning_tree = []
    edge_number, vertice_count = 0, len(Graph)
    selected = [False] * vertice_count

    if start_index < 0:
        selected[np.random.randint((vertice_count - 1))] = True
    else:
        selected[start_index] = True

    while edge_number < vertice_count - 1:
        minimum = Decimal("Infinity")
        minEdge = {}
        for V1 in range(vertice_count):
            if selected[V1]:
                for V2 in range(vertice_count):
                    if ((not selected[V2]) and Graph[V1][V2]):
                        if minimum > Graph[V1][V2]:
                            minimum = Graph[V1][V2]
                            minEdge = {
                                "V1": V1,
                                "V2": V2,
                                "W": minimum
                            }

        selected[minEdge["V2"]] = True
        minimum_spanning_tree.append(minEdge)
        edge_number += 1

    return minimum_spanning_tree


def ParseGraph(filename):
    GraphMatrix = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            # Casting str to int....
            GraphMatrix.append(list(map(int, line.split())))
    return GraphMatrix

def Output(filename, result):
    with open(filename, 'w') as file:
        totalWeight = 0
        for edge in result:
            file.write(str(edge["V1"]) + " - " + str(edge["V2"]) + "\t")
            totalWeight += edge["W"]
        file.write("\nMinimum Spanning Tree Weight: " + str(totalWeight))


# Graph-Matrix Neighborhood List:
""" G = [[0, 3, 1, 5, 0, 0],
     [3, 0, 0, 13, 0, 7],
     [1, 0, 0, 4, 2, 6],
     [5, 13, 4, 0, 0, 6],
     [0, 0, 2, 0, 0, 12],
     [0, 7, 6, 6, 12, 0]] """

G = ParseGraph("input.txt")
result = minimum_spanning_tree(G, 1)
print(result)
Output("output.txt", result)
