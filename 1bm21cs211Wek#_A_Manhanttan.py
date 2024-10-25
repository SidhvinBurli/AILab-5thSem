import heapq

class PuzzleState:
    def __init__(self, board, g=0, goal=None):
        self.board = board
        self.g = g   
        self.goal = goal if goal is not None else [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.h = self.manhattan_distance()
        self.f = self.g + self.h
        self.zero_pos = board.index(0)   

    def manhattan_distance(self):
        distance = 0
        for index, tile in enumerate(self.board):
            if tile != 0:  
                goal_index = self.goal.index(tile)
               
                current_x, current_y = divmod(index, 3)
                goal_x, goal_y = divmod(goal_index, 3)
                distance += abs(current_x - goal_x) + abs(current_y - goal_y)
        return distance

    def get_neighbors(self):
        moves = []
        x, y = divmod(self.zero_pos, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_zero_pos = nx * 3 + ny
                new_board = self.board[:]
                new_board[self.zero_pos], new_board[new_zero_pos] = new_board[new_zero_pos], new_board[self.zero_pos]
                moves.append(PuzzleState(new_board, self.g + 1, self.goal))
        return moves

     
    def __lt__(self, other):
        return self.f < other.f

def a_star(initial_board, goal_state):
    start_state = PuzzleState(initial_board, goal=goal_state)
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.h == 0:   
            return current_state   

        closed_set.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue
            
            heapq.heappush(open_list, neighbor)

    return None  # No solution

def input_board(prompt):
    board = []
    print(prompt)
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers, space-separated): ").strip().split()
        if len(row) != 3:
            print("Invalid row. Please enter exactly 3 numbers.")
            return None
        board.extend(int(num) for num in row)
    return board

def main():
     
    initial_state = input_board("Enter the initial state of the puzzle:")
    if initial_state is None or len(initial_state) != 9 or set(initial_state) != set(range(9)):
        print("Invalid input for initial state. Please enter 9 unique numbers from 0 to 8.")
        return

   
    goal_state = input_board("Enter the goal state of the puzzle:")
    if goal_state is None or len(goal_state) != 9 or set(goal_state) != set(range(9)):
        print("Invalid input for goal state. Please enter 9 unique numbers from 0 to 8.")
        return

     
    solution = a_star(initial_state, goal_state)

  
    if solution is None:
        print("No solution found.")
    else:
        print("Solution found!")
        print("Final board state:", solution.board)

if __name__ == "__main__":
    main()
2