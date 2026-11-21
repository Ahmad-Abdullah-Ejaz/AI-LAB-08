
# Task 1: Find goal node G using Greedy Best First Search.

class Graph:
    def __init__(self):
        # Store each node and its connected neighbours.
        self.adj = {}

    def addEdge(self, u, v):
        # Create an empty list if node is not present.
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        # Add an undirected edge.
        self.adj[u].append(v)
        self.adj[v].append(u)

    def greedyBestFirstSearch(self, start, goal, heuristic):

        # Store nodes according to heuristic values.
        open_list = [start]

        # Track visited nodes.
        visited = set()

        # Store the parent of each node.
        parent = {start: None}

        while open_list:

            # Find the node with lowest heuristic value.
            current = open_list[0]

            for node in open_list:
                if heuristic[node] < heuristic[current]:
                    current = node

            # Remove selected node from OPEN list.
            open_list.remove(current)

            # Skip if already visited.
            if current in visited:
                continue

            # Mark current node as visited.
            visited.add(current)

            print("Visiting:", current)

            # Check whether goal is reached.
            if current == goal:

                path = []
                node = goal

                while node is not None:
                    path.append(node)
                    node = parent[node]

                path.reverse()

                print("Goal Found!")
                print("Path:", " -> ".join(path))
                return

            # Explore neighbours of current node.
            for neighbour in self.adj[current]:

                if neighbour not in visited:

                    if neighbour not in parent:
                        parent[neighbour] = current

                    if neighbour not in open_list:
                        open_list.append(neighbour)

        print("Goal not found!")


# Create graph object.
g = Graph()

# Add edges to the graph.
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('C', 'G')

# Define heuristic values.
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 4,
    'G': 0
}

# Run Greedy Best First Search.
g.greedyBestFirstSearch('A', 'G', heuristic)
