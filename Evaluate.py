# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:59:39 2019

@author: Mila
"""
def check_pair(pair):
    with open("ytcom.txt") as f:
        for line in f:
            edges = tuple([int(x) for x in line.strip().split("\t")])
            if pair[0] in edges and pair[1] in edges:
                return True
        return False

"""
Returns list of pairs of nodes which were clustered together
"""
def get_pairs(communities):
    pairs = list()
    for community in communities:
        num_nodes = len(community)
        if num_nodes > 1:
            for i in range(1, num_nodes):
                pairs.append([community[i-1], community[i]])      
    return pairs

"""
Returns list of pairs of nodes that were not clustered together
"""
def get_non_pairs(visited, pairs):
    non_pairs = list()
    for i in range(1, len(visited)):
        pair = [visited[i-1], visited[i]]
        if not pair in pairs:
            non_pairs.append(pair)
    return non_pairs

"""
Penalizes false positives and false negatives
Rewards true positives and true negatives

Interpretation:
A score close to 0 is very bad
A score over 1 is good, the greater the better

:param pairs: list of pairs of sampled nodes which ended up in the same community
:param non-pairs: list of all possible pairs in the sample that did not end up in the same community
"""
def score(pairs, non_pairs):
    score = 1.0
    for pair in pairs:
        if(check_pair(pair)): # TP
            score *= 1.1
        else:
            score *= 0.9 # FP
    for pair in non_pairs:
        if(check_pair(pair)): # FN
            score *= 0.9
        else:
            score *= 1.1 # TN
    return score
        
