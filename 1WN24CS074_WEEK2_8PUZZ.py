# 8-puzzle solved with Depth-Limited DFS.  State = tuple of 9 numbers, 0 = blank.
#   index layout:  0 1 2
#                  3 4 5
#                  6 7 8

initial = (5, 4, 0,
           6, 1, 8,
           7, 3, 2)
goal    = (0, 1, 2,
           3, 4, 5,
           6, 7, 8)

# blank at index i can swap with these neighbour indices
moves = {0: [1, 3],       1: [0, 2, 4],    2: [1, 5],
         3: [0, 4, 6],    4: [1, 3, 5, 7], 5: [2, 4, 8],
         6: [3, 7],       7: [4, 6, 8],    8: [5, 7]}


def get_children(state):
    """All boards reachable by sliding one tile into the blank."""
    b = state.index(0)
    children = []
    for n in moves[b]:
        s = list(state)
        s[b], s[n] = s[n], s[b]
        children.append(tuple(s))
    return children


def is_solvable(state):
    """Half of all 8-puzzle boards can never reach the goal.
    Rule: count inversions (pairs of tiles in the wrong order, ignoring 0);
    for a 3x3 board the puzzle is solvable only if the count is even."""
    tiles = [x for x in state if x != 0]
    inversions = sum(1 for i in range(len(tiles))
                       for j in range(i + 1, len(tiles))
                       if tiles[i] > tiles[j])
    return inversions % 2 == 0


def dfs(state, goal, limit, path, best_depth):
    """Depth-limited DFS. Returns the path to goal, or None.
    path       : boards from start to current state
    best_depth : state -> shallowest depth at which we already expanded it"""
    depth = len(path) - 1
    if state == goal:
        return path
    if depth == limit:                      # not allowed to go deeper
        return None
    for child in get_children(state):
        # skip if we already explored this board at the same or a shallower depth
        if best_depth.get(child, limit + 1) <= depth + 1:
            continue
        best_depth[child] = depth + 1
        result = dfs(child, goal, limit, path + [child], best_depth)
        if result is not None:
            return result
    return None


def show(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) if x else '_' for x in state[i:i + 3]))
    print()

print("output USN : 1WN24CS074")

if __name__ == "__main__":
    if not is_solvable(initial):
        print("This puzzle cannot be solved.")
    else:
        LIMIT = 30
        path = dfs(initial, goal, LIMIT, [initial], {initial: 0})
        if path is None:
            print("No solution within depth limit", LIMIT)
        else:
            print("Solved in", len(path) - 1, "moves\n")
            for step, s in enumerate(path):
                print("Step", step)
                show(s)