from typing import Set, List, Dict
from graph_base_class import Edge

class Node:
    def __init__(self, name : str, id : int, location) -> None:
        self.name = name 
        self.id = id 
        self.location = location 

class Edge:
    def __init__(self, start, finish, weight) -> None:
        self.start = start
        self.finish = finish
        self.weight = weight
# Implement Graph using an adjacency list as the underlying representation
class AdjacencyListGraph():

    # if is_directed is true, this should be a directed graph.  If false, it's an undirected graph
    # Make sure your implementation accounts for node order on an edge for directed and is neutral for undirected
    # super sets a property self.is_directed to the parameter value
    def __init__(self, is_directed:bool) -> None:
        self.is_directed = is_directed
        # set in self.nodes is for the edges 
        self.nodes : Dict[int,Set] = dict()
        self.id_to_nodes : Dict[int, Node] = dict()
    
    # Adds a node named "name" to the graph.
    def add_node(self, id, name, location) -> None:
        #written by Klaka
        self.nodes.setdefault(id, set())
        self.id_to_nodes.setdefault(id, Node(name, id, location))

    
    # Gets a set of the names of all nodes in the graph
    def get_nodes(self) -> Set[any]:
        return set(self.nodes.keys())

    # Adds an edge from node start to node finish with the weight specified
    def add_edge(self, start:any, finish:any, weight:int) -> None:
        new_edge = Edge(start, finish, weight)
        self.nodes[start].add(new_edge)


    # Gets a set of edges leading out of the given node
    def get_edges(self, id: int) -> Set[Edge]:
        return self.nodes.get(id)