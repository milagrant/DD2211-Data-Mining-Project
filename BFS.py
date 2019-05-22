# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:32:39 2019

@author: Mila
"""
import csv
import queue
import random

FULL = 1134890
SAMPLE = FULL*0.01
fr = list()
to = list()
    
def init():
    global fr
    global to
    with open('ytgraph.txt.') as f:
        reader = csv.reader(f, delimiter="\t")
        first_col = list(zip(*reader))[0]
        fr = list(map(int, first_col))
    
    with open('ytgraph.txt') as f:
        reader = csv.reader(f, delimiter="\t")
        second_col = list(zip(*reader))[1]
        to = list(map(int, second_col))
        
def gen_random_sample():
    init()
    indices = random.sample(range(1, FULL), SAMPLE)
    visited = list()
    edges = list()
    for i in range(1, FULL):
        if i in indices:
            node_from = fr[i]
            node_to = to[i]
            edges.append([node_from, node_to])
            if not node_from in visited:
                visited.append(node_from)
            if not node_to in visited:
                visited.append(node_to)
    return edges, visited
                  
def bfs(root):
     Q = queue.Queue()
     Q.put(root)
     visited = list()     
     visited.append(root)     
     edges = list()
     
     while len(visited) < SAMPLE and not Q.empty():        
         current = Q.get()
         neighbours = list()
         for i in range(FULL):
             if fr[i] == current:
                 neighbours.append(to[i])
             if to[i] == current:
                 neighbours.append(fr[i])
         for n in neighbours:
             if n in visited:
                 continue
             Q.put(n)
             visited.append(n)
             edges.append([current, n])
    
     return edges, visited
 
def gen_bfs_sample():
    init()
    root = random.randint(1,FULL)
    return bfs(root)

