# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:56:55 2019

@author: Mila
"""
from BFS import gen_bfs_sample, gen_random_sample
from Evaluate import get_pairs, get_non_pairs, score
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

def get_results(visited, clustering):
    communities = list()
    num_communities = max(clustering)
    for i in range(num_communities +1):
        community = list()
        for j in range(len(clustering)):
            if clustering[j] == i:
                community.append(index_map[j])
        communities.append(community) 
    return communities
        
def main():
    adj_list, visited = gen_random_sample()
    #adj_list, visited = gen_bfs_sample()
    create_index(visited)
    matrix = adj_list_to_matrix(adj_list, len(visited))
    clustering = SpectralClustering(assign_labels='kmeans').fit_predict(matrix)
    communities = get_results(visited, clustering)
    pairs = get_pairs(communities)
    non_pairs = get_non_pairs(visited, pairs)
    print(score(pairs, non_pairs))

if __name__== "__main__":
    main()
