import heapq

class PuzzleState:
    def __init__(self, board, g, h):
        self.board = board   
        self.g = g  
        self.h = h  
        self.f = g + h  

    def __lt__(self, other):
        return self.f < other.f    

def print_board(board):
    """Print the current board state."""
    for row in board:
        print(" ".join(str(num) for num in row))
    print()   

def get_blank_position(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  
                return (i, j)

def get_successors(state):
    successors = []
    x, y = get_blank_position(state.board)   
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:   
            new_board = [row[:] for row in state.board]  
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]   
            successors.append(PuzzleState(new_board, state.g + 1, 0))   
    return successors

def heuristic_manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                target_x = (board[i][j] - 1) // 3
                target_y = (board[i][j] - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

def is_goal_state(board):
    return board == [[1, 2, 3], 
                     [8, 0, 4], 
                     [7, 6, 5]]  

def a_star_search_manhattan_distance(start_board):
    start_state = PuzzleState(start_board, 0, heuristic_manhattan_distance(start_board))
    open_set = []
    heapq.heappush(open_set, start_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)
         print("Current board state:")
        print_board(current_state.board)
        print(f"g(n): {current_state.g}, h(n): {current_state.h}, f(n): {current_state.f}\n")

        
        if is_goal_state(current_state.board):
            print("Goal state reached!")
            return current_state.g   

        closed_set.add(tuple(map(tuple, current_state.board)))

        for successor in get_successors(current_state):
            successor.h = heuristic_manhattan_distance(successor.board)
            successor.f = successor.g + successor.h

            if tuple(map(tuple, successor.board)) in closed_set:
                continue

            heapq.heappush(open_set, successor)

    return None   

def get_user_input():
    board = []
    for i in range(3):
        while True:
            row = input(f"Enter row {i + 1} (3 numbers separated by space): ")
            nums = list(map(int, row.split()))
            if len(nums) == 3 and all(0 <= num <= 8 for num in nums):
                board.append(nums)
                break
            else:
                print("Invalid input. Please enter 3 numbers between 0 and 8.")
    return board

if __name__ == "__main__":
    start_board = get_user_input()
    steps = a_star_search_manhattan_distance(start_board)
    print(f"Steps to solve with Manhattan Distance heuristic: {steps}")
