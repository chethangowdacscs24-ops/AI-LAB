# 8-puzzle solved with Iterative Deepening DFS (IDFS).
# State = tuple of 9 numbers, 0 = blank.
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


def get_children(state):
    b = state.index(0)
    children = []
    for n in moves[b]:
        s = list(state)
        s[b], s[n] = s[n], s[b]
        children.append(tuple(s))
    return children


def depth_limited_dfs(start, goal, limit):
    """DFS that refuses to go deeper than `limit` moves.
    Only checks the CURRENT path for repeats, not a global visited set,
    so the same board can be revisited at a different depth in another branch."""
    stack = [(start, [start])]
    while stack:
        state, path = stack.pop()
        depth = len(path) - 1

        if state == goal:
            return path
        if depth == limit:
            continue

        for child in get_children(state):
            if child not in path:
                stack.append((child, path + [child]))
    return None


def idfs(start, goal, max_limit=50):
    for limit in range(max_limit + 1):
        result = depth_limited_dfs(start, goal, limit)
        if result is not None:
            return result, limit
    return None, None


def show(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) if x else '_' for x in state[i:i + 3]))
    print()


print("output (1WN24CS074):")
if __name__ == "__main__":
    path, limit = idfs(initial, goal)
    if path is None:
        print("No solution found within max limit.")
    else:
        print("Solution found at depth limit", limit)
        print("Solved in", len(path) - 1, "moves\n")
        for step, s in enumerate(path):
            print("Step", step)
            show(s)