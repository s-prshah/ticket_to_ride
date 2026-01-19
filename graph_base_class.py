from abc import ABC, abstractmethod
from typing import Set, Dict


class Edge:
    def __init__(self, start, finish, weight) -> None:
        self.start = start
        self.finish = finish
        self.weight = weight

class GraphBaseClass(ABC):
    def __init__(self, is_directed: bool) -> None:
        self.is_directed = is_directed
        self.nodes : Dict[str, Set[Edge]] = {"name" : (Edge)}
        super().__init__()

    @abstractmethod
    def add_node(self, name:any) -> None:
        self.nodes[name] = set()

    @abstractmethod
    def remove_node(self, name:any) -> None:
        if name in self.nodes:
            for n in self.nodes:
                new_set = set()
                for e in self.nodes[n]:
                    if e.finish == name:
                        new_set.add(e)
                self.nodes[n] = self.nodes[n].difference(new_set)
            self.nodes.pop(name)
                    

    @abstractmethod
    # return True if the node name1 is connected to the node name2 and False otherwise
    def is_connected(self, name1:any, name2:any) -> bool:
        if name1 in self.nodes:
            for e in self.nodes[name1]:
                if e.start == name1 and e.finish == name2:
                    return True
        return False 

    @abstractmethod
    def add_edge(self, start:any, finish:any, weight:int) -> None:
        self.nodes[start].add(Edge(start, finish, weight))

    @abstractmethod
    # Returns a set of node names adjacent to the given node (i.e. there's an arc from the node to the neighbor)
    def get_neighbors(self, name:any) -> Set[any]:
        all_neighbors = set()
        for i in self.nodes:
            for e in self.nodes[i]:
                if e.finish == name:
                    all_neighbors.add(e.start)
                elif e.start == name:
                    all_neighbors.add(e.finish)
        return all_neighbors
    
    @abstractmethod
    # Gets a set of arcs leading out of the given node
    def get_edges(self, name:any) -> Set[Edge]:
        all_edges = set()
        for i in self.nodes[name]:
            all_edges.add(i)
        return all_edges
    
    @abstractmethod
    # Gets a set of arcs leading out of the given node
    def get_nodes(self, name:str) -> Set[str]:
        all_nodes = set()
        for i in self.nodes[name]:
            all_nodes.add(i.finish)
        return all_nodes