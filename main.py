import timeit

import numpy as np

with open("graph.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=",")

print(array)

class Graph:
    def __init__(self):
        pass

    def read(self, v):
        self.data = v
        self.size = len(v)

    def findMinimum(self, E):
        val = E[0]
        for i in range(len(E)):
            if val[2] > E[i][2]:
                val = E[i]
        return val

    def process(self):
        T = [False] * self.size
        L = []
        E = []

        for i in range(self.size):
            if i == 0:
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range(j, self.size):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                targetEdge = self.findMinimum(E)
                L.append(targetEdge)
                T[targetEdge[0]] = True
                # T[targetEdge[1]] = True
                E = []

        print(L)
        length = 0
        for ele in L:
            length = length + ele[2]
        print('Minimum Spanning Tree Length is: ', length)

g = Graph()

def startFunction():
    g.read(array)
    g.process()

print(timeit.Timer(startFunction).timeit(number=5))