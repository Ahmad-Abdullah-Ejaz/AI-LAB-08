
# Task 2: Find goal node G using A* Search.

class Graph:
    def __init__(self):
        # Store each node and its connected neighbours with edge costs.
        self.adj = {}

    def addEdge(self, u, v, w):
        # Create an empty list if node is not present.
        if u not in self.adj:
            self.adj[u] = []

        if v not in self.adj:
            self.adj[v] = []

        # Add an undirected weighted edge.
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def aStarSearch(self, start, goal, heuristic):

        # Store nodes that are waiting to be explored.
        open_list = [start]

        # Store nodes that have already been expanded.
        closed_list = set()

        # Store actual cost from start to each node.
        g_cost = {start: 0}

        # Store parent of each node.
        parent = {start: None}

        while open_list:

            # Select node having lowest f(n) = g(n) + h(n).
            current = open_list[0]

            for node in open_list:
                if (g_cost[node] + heuristic[node]) < (
                    g_cost[current] + heuristic[current]
                ):
                    current = node

            # Remove selected node from OPEN list.
            open_list.remove(current)

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
                print("Total Cost:", g_cost[goal])
                return

            # Mark current node as expanded.
            closed_list.add(current)

            print("Visiting:", current)

            # Explore neighbours of current node.
            for neighbour, weight in self.adj[current]:

                # Calculate new actual path cost.
                new_cost = g_cost[current] + weight

                # Check whether a better path is found.
                if neighbour not in g_cost or new_cost < g_cost[neighbour]:

                    # Update actual cost.
                    g_cost[neighbour] = new_cost

                    # Update parent of neighbour.
                    parent[neighbour] = current

                    # If node was already expanded, reopen it.
                    if neighbour in closed_list:
                        closed_list.remove(neighbour)

                    # Add neighbour to OPEN list if not present.
                    if neighbour not in open_list:
                        open_list.append(neighbour)

        print("Goal not found!")


# Create graph object.
g = Graph()

# Add weighted edges to the graph.
g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 4)
g.addEdge('B', 'D', 2)
g.addEdge('B', 'E', 5)
g.addEdge('C', 'F', 2)
g.addEdge('D', 'G', 5)
g.addEdge('E', 'G', 2)
g.addEdge('F', 'G', 3)

# Define heuristic values.
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 3,
    'G': 0
}

# Run A* Search.
g.aStarSearch('A', 'G', heuristic)
