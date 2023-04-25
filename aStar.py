from queue import PriorityQueue

def manhattan_distance(board):
    return sum(abs((val-1)%3 - j) + abs((val-1)//3 - i)
               for i, row in enumerate(board) for j, val in enumerate(row) if val)

def solve(initial_state, goal_state):
    frontier = PriorityQueue()
    frontier.put((manhattan_distance(initial_state), initial_state))
    came_from = {str(initial_state): None}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal_state:
            path = []
            while current != initial_state:
                path.append(current)
                current = came_from[str(current)]
            path.append(initial_state)
            path.reverse()
            return path

        for i, row in enumerate(current):
            for j, val in enumerate(row):
                if not val:
                    for d_row, d_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_row, new_col = i + d_row, j + d_col
                        if 0 <= new_row < 3 and 0 <= new_col < 3:
                            new_state = [row[:] for row in current]
                            new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]

                            if str(new_state) not in came_from:
                                frontier.put((manhattan_distance(new_state), new_state))
                                came_from[str(new_state)] = current
                                

    return None

initial_state = [[1,2,3], [0,4,6], [7,5,8]]
goal_state = [[1, 2, 3], [4,5,6], [7,8,0]]
path = solve(initial_state, goal_state)
print("Path: ")
for state in path:
    print("-------")  
    for row in state:
        print(end="")
        for val in row:
            if val == 0:
                print(" ", end="\t")
            else:
                print(val, end="\t")
        print(" ")