
# Task 3: Solve 8 Puzzle using A* Search

class Puzzle:
    def misplacedTiles(self, state, goal):
        count = 0

        for i in range(9):
            if state[i] != 0 and state[i] != goal[i]:
                count += 1

        return count

    def getNeighbors(self, state):
        neighbors = []

        # Find the position of empty space (0).
        empty = state.index(0)

        row = empty // 3
        col = empty % 3

        # Possible movements: Up, Down, Left, Right.
        moves = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

        for new_row, new_col in moves:

            # Check whether the new position is inside the grid.
            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_position = new_row * 3 + new_col

                new_state = list(state)

                # Move the adjacent tile into the empty space.
                new_state[empty], new_state[new_position] = (
                    new_state[new_position],
                    new_state[empty]
                )

                neighbors.append(tuple(new_state))

        return neighbors

    def printBoard(self, state):
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()

    def aStarSearch(self, initial, goal):

        open_list = [initial]
        closed_list = set()

        g_cost = {initial: 0}
        parent = {initial: None}

        while open_list:

            # Select the state having the lowest f(n).
            current = open_list[0]

            for state in open_list:
                f1 = g_cost[state] + self.misplacedTiles(state, goal)
                f2 = g_cost[current] + self.misplacedTiles(current, goal)

                if f1 < f2:
                    current = state

            open_list.remove(current)

            # Check whether the goal state is reached.
            if current == goal:

                path = []
                state = current

                while state is not None:
                    path.append(state)
                    state = parent[state]

                path.reverse()

                print("Goal Found!")
                print("Total Moves:", g_cost[goal])
                print("Solution Path:\n")

                for i, state in enumerate(path):
                    print("Step", i)
                    self.printBoard(state)

                return

            closed_list.add(current)

            # Generate all possible next states.
            for neighbor in self.getNeighbors(current):

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                    g_cost[neighbor] = new_cost
                    parent[neighbor] = current

                    if neighbor in closed_list:
                        closed_list.remove(neighbor)

                    if neighbor not in open_list:
                        open_list.append(neighbor)

        print("Goal not found!")


# Create Puzzle object.
p = Puzzle()

# Initial state (0 represents empty space).
initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

# Required goal state.
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

# Call A* Search.
p.aStarSearch(initial, goal)
