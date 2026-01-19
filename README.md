# Ticket to Ride – Pathfinding + Graph Algorithms (Python)

A Python implementation of core **Ticket to Ride-style routing logic**, focused on graph modeling and shortest-path computation. Built a custom **adjacency list graph** and implemented **A\*** pathfinding using heuristics to compute optimal routes between cities.

> Note: Completed as part of a coursework project. All code shown here was implemented by me and is included in my portfolio.

---

## Features
- Graph representation using an adjacency list
- Node + edge modeling with weighted connections
- A\* pathfinding with a distance heuristic (Euclidean)
- Route reconstruction returning:
  - ordered city-to-city path
  - total route cost

---

## Key Components
- `AdjacencyListGraph`
  - `add_node()`, `add_edge()`, `get_edges()`
- `PathFinder`
  - `get_minimum_path(start_id, destination_id)` → returns `RouteInfo`
- Custom `PriorityQueue` for open-set management in A\*

---

## Concepts & Data Structures
- Graphs (weighted edges)
- Priority queue / heap concepts
- A\* shortest path search
- Heuristics + backpointer-based path reconstruction

---

## Author
**Prisha Shah**
