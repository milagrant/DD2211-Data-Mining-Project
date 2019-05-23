import networkx as nx
import numpy as np
import os
import random

complete_graph = nx.Graph()
num_nodes = 0

def init():
    global complete_graph
    global num_nodes
    
    with open('youtube.dat') as f:
        edges = [tuple([int(x) for x in line.strip().split("\t")]) for line in f]

    nodes = np.unique(np.asarray(edges))
    num_nodes = nodes.shape[0]

    complete_graph.add_nodes_from(nodes)
    complete_graph.add_edges_from(edges)

def random_walk_sample(graph, num_sample):
    for i, data in graph.nodes(data=True):
        graph.node[i]['id'] = i
    
    sampled_graph = nx.Graph()
    
    root_idx = random.randint(1, num_nodes)
    sampled_graph.add_node(graph.node[root_idx]['id'])
    
    curr_node = root_idx
    
    while sampled_graph.number_of_nodes() != num_sample:
        neighbor_nodes = [n for n in graph.neighbors(curr_node)]
        selected_idx = random.randint(0, len(neighbor_nodes) - 1)
        selected_node = neighbor_nodes[selected_idx]
        
        sampled_graph.add_node(selected_node)
        sampled_graph.add_edge(curr_node, selected_node)
        curr_node = selected_node
    
    return sampled_graph

def random_jump_sample(graph, num_sample):
    iter_ = 1
    edges_num = 0
    
    for i, data in graph.nodes(data=True):
        graph.node[i]['id'] = i
    
    sampled_graph = nx.Graph()
    
    root_idx = random.randint(1, num_nodes)
    sampled_graph.add_node(graph.node[root_idx]['id'])
    
    curr_node = root_idx
    
    while sampled_graph.number_of_nodes() != num_sample:
        neighbor_nodes = [n for n in graph.neighbors(curr_node)]
        selected_idx = random.randint(0, len(neighbor_nodes) - 1)
        selected_node = neighbor_nodes[selected_idx]
        
        sampled_graph.add_node(selected_node)
        sampled_graph.add_edge(curr_node, selected_node)
        curr_node = selected_node
        
        if iter_ % 100 == 0:
            print("masuk pak eko")
            if ((sampled_graph.number_of_edges() - edges_num) < 2):
                curr_node = random.randint(1, num_nodes)
            edges_num = sampled_graph.number_of_edges()
            
    return sampled_graph

def generate_rw_sample(pct_sample):
    init()
    sampled_graph = random_walk_sample(complete_graph, int(pct_sample*num_nodes))
    adj_m_sampled_graph = nx.adjacency_matrix(sampled_graph).todense()
    return sampled_graph, adj_m_sampled_graph

def generate_rj_sample(pct_sample):
    init()
    sampled_graph = random_jump_sample(complete_graph, int(pct_sample*num_nodes))
    adj_m_sampled_graph = nx.adjacency_matrix(sampled_graph).todense()
    return sampled_graph, adj_m_sampled_graph