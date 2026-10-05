import heapq

# 8-puzzle solved with A* search, printing g(n), h(n), f(n) for every
# state on the final solution path.  State = tuple of 9 numbers, 0 = blank.
#   index layout:  0 1 2
#                  3 4 5
#                  6 7 8

initial = (5, 4, 0,
           6, 1, 8,
           7, 3, 2)
goal    = (0, 1, 2,
           3, 4, 5,
           6, 7, 8)

moves = {0: [1, 3],       1: [0, 2, 4],    2: [1, 5],
         3: [0, 4, 6],    4: [1, 3, 5, 7], 5: [2, 4, 8],
         6: [3, 7],       7: [4, 6, 8],    8: [5, 7]}

goal_pos = {value: (i // 3, i % 3) for i, value in enumerate(goal)}


def get_children(state):
    b = state.index(0)
    children = []
    for n in moves[b]:
        s = list(state)
        s[b], s[n] = s[n], s[b]
        children.append(tuple(s))
    return children


def heuristic(state):
    """Manhattan distance: sum over tiles of |row diff| + |col diff|."""
    total = 0
    for i, v in enumerate(state):
        if v == 0:
            continue
        r1, c1 = i // 3, i % 3
        r2, c2 = goal_pos[v]
        total += abs(r1 - r2) + abs(c1 - c2)
    return total


def a_star(start, goal):
    g = {start: 0}
    parent = {start: None}
    frontier = [(heuristic(start), start)]      # (f, state)

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for child in get_children(current):
            new_g = g[current] + 1
            if child not in g or new_g < g[child]:
                g[child] = new_g
                parent[child] = current
                f = new_g + heuristic(child)
                heapq.heappush(frontier, (f, child))

    return None


def show(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) if x else '_' for x in state[i:i + 3]))
    print()

print("output (1WN24CS074):")
if __name__ == "__main__":
    path = a_star(initial, goal)
    if path is None:
        print("No solution.")
    else:
        print("Solved in", len(path) - 1, "moves\n")
        for step, s in enumerate(path):
            gn = step                    # moves taken so far = depth
            hn = heuristic(s)
            fn = gn + hn
            print(f"Step {step}:  g(n) = {gn},  h(n) = {hn},  f(n) = {fn}")
            show(s)