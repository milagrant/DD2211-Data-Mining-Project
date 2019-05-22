# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:56:55 2019

@author: Mila
"""
from BFS import gen_bfs_sample
from sklearn.cluster import SpectralClustering
import numpy as np

index_map = dict()
reversed_index_map = dict()
    
def create_index(visited):
    global index_map
    i = 0
    for node in visited:
        index_map[i] = node
        reversed_index_map[node] = i
        i += 1

def adj_list_to_matrix(adj_list, length):
    matrix = np.zeros((length, length))
    for i in index_map:
        node = index_map[i]
        for edge in adj_list:
            if edge[0] == node:
                matrix[i][reversed_index_map[edge[1]]] = 1
            if edge[1] == node:
                matrix[i][reversed_index_map[edge[0]]] = 1
    return matrix

def main():
    adj_list, visited = gen_bfs_sample()
    create_index(visited)
    matrix = adj_list_to_matrix(adj_list, len(visited))
    clustering = SpectralClustering(assign_labels="discretize").fit_predict(matrix)
    print(clustering)

if __name__== "__main__":
  main()
