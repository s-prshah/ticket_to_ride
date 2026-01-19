from math import sqrt
import sys
from typing import Dict, List, Set, Tuple
from priority_queue import PriorityQueue
from graph_base_class import Edge, GraphBaseClass
from adjacency_list import AdjacencyListGraph, Node

# You do not need to change this class.  It is used as the return type for get_minimum_path
class RouteInfo:
    def __init__(self, 
                 route: List[Tuple[str, str]], # list of tuples of friendly names for the start and destination cities
                 route_ids: List[Tuple[int, int]], # list of tuples of ids for the start and destination cities
                 cost: int) -> None: # the total cost of the route from start to destination
        self.route = route
        self.route_ids = route_ids
        self.cost = cost

# TODO: Implement the methods on the PathFinder class using an underlying graph representation
# of your choice. Feel free to use your graph classes from the practice exercises; copy the appropriate
# files into your project and import the classes at the top of this file.
# NOTE: You can assume that graphs are directed
class PathFinder:
    def __init__(self) -> None:
        self.cur_graph = AdjacencyListGraph(False)
        self.all_nodes : Dict[int, Node] = self.cur_graph.id_to_nodes
        #self.all_nodes_dict has the Node, cost, and the node name it came from 
        self.all_nodes_dict : Dict[int, Dict[str, any]] = {}


    # TODO: adds an edge to the graph, using a the id of the start node and id of the finish node
    # NOTE: You can assume that graphs are directed and do not have to add multiple edges here (extra edges should be added by the caller)
    def add_edge(self, start_id: int, finish_id:int , cost: float) -> None:
        self.cur_graph.add_edge(start_id, finish_id, cost)

    # TODO: adds a node to the graph, passing in the id, friendly name, and location of the node.
    # location is a tuple with the x and y coordinates of the location
    def add_node(self, id: int, name: str, location: Tuple[float, float]) -> None:
        self.cur_graph.add_node(id, name, location)

    # TODO: calculates the minimum path using the id of the start city and id of the destination city, using A*
    # Returns a RouteInfo object that contains the edges for the route.  See RouteInfo above for attributes
    # Note: This implementation must use A* to get full credit. 
    def get_minimum_path(self, start_city_id: int, destination_id:int ) -> RouteInfo:
        all_routes = RouteInfo([], [], 0)
        queue = PriorityQueue()

        # for id in self.cur_graph.get_nodes():
        #     self.all_nodes[id] = self.cur_graph.id_to_nodes[id]
        final_node_location = self.all_nodes[destination_id].location
        visited : Set[int] = set()

        for id in self.cur_graph.get_nodes():
            self.all_nodes_dict[id] = {"cost" : False, "prev_node_id": None}
        
        self.all_nodes_dict[start_city_id]["cost"] = 0
        self.all_nodes_dict[start_city_id]["prev_node_id"] = start_city_id
        cost = 0
        queue.enqueue(cost, start_city_id)

        while queue.size() > 0:
            cur_id = queue.dequeue()
            if cur_id in visited:
                continue
            visited.add(cur_id)

            if cur_id == destination_id:
                break

            for e in self.cur_graph.get_edges(cur_id):
                #heuristic_cost is ONLY used to find the priority 
                heuristic_cost = self.distance_calc(self.all_nodes[e.finish].location, final_node_location)
                total_cost = self.all_nodes_dict[cur_id]["cost"] + e.weight 
                if self.all_nodes_dict[e.finish]["cost"] == False:
                    self.all_nodes_dict[e.finish] = {"cost": total_cost, "prev_node_id": e.start}
                    queue.enqueue(total_cost + heuristic_cost, e.finish)
                else:
                    if total_cost < self.all_nodes_dict[e.finish]["cost"]:
                        self.all_nodes_dict[e.finish] = {"cost": total_cost, "prev_node_id": e.start}
                        queue.enqueue(total_cost + heuristic_cost, e.finish)

        cur_id = destination_id
        while cur_id != start_city_id:
            prev_id = self.all_nodes_dict[cur_id]["prev_node_id"]
            all_routes.route_ids.append((prev_id, cur_id))
            all_routes.route.append((self.all_nodes[prev_id].name, self.all_nodes[cur_id].name))
            cur_id = prev_id
        
        all_routes.cost = self.all_nodes_dict[destination_id]["cost"]
             
        return all_routes
            
    #pass in each location as tuple (location1, location2) -> used for heuristic cost in A*
    def distance_calc(self, point1 : Tuple, point2: Tuple) -> int:
        dif1 = point2[0] - point1[0]
        dif2 = point2[1] - point1[1]
        distance = sqrt((dif1**2) + (dif2**2))
        return distance
    



