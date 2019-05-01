# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:39:14 2019

@author: Mila
"""
import os


"""
Goes through this directory and appends the content of all .edges files into
compiled.txt, as well as a new line for each egonode-node edge. 
Excludes duplicate edges.
"""

directory = "./twitter"
outfile = "complied.txt"
edges_seen = set()
out = open(outfile, "w")
for filename in os.listdir(directory):
    if filename.endswith(".edges"):
        pathname = "./" + directory + "/" + filename
        f = open(pathname, "r")
        ego = filename.split(".")[0]
        lines = f.readlines()
        for line in lines:
            if line not in edges_seen:
                out.write(line)
                edges_seen.add(line)
            nodes = line.split(" ")
            new_edge = ego + " " + nodes[0] + "\n"
            if not new_edge in edges_seen:
                out.write(new_edge)
                edges_seen.add(new_edge)
            new_edge = ego + " " + nodes[1]
            if not new_edge in edges_seen:
                out.write(new_edge)
                edges_seen.add(new_edge)
f.close
out.close