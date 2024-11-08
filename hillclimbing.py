import random

def get_user_board(n):
    board = []
    print(f"Enter the initial row positions for each column (0 to {n-1}):")
    for col in range(n):
        row = int(input(f"Column {col + 1}: "))
        if 0 <= row < n:
            board.append(row)
        else:
            print("Invalid input. Row must be between 0 and", n - 1)
            return None
    return board

def heuristic(board):
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def get_neighbors(board):
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if board[col] != row:
                neighbor = board[:]
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing_with_restarts(n, initial_board):
    current = initial_board
    iteration = 0
    while True:
        while True:
            current_heuristic = heuristic(current)
            print(f"Iteration {iteration}, Heuristic: {current_heuristic}")
            print_board(current)
            iteration += 1
            
            if current_heuristic == 0:
                return current
            
            neighbors = get_neighbors(current)
            best_neighbor = min(neighbors, key=heuristic)
            best_neighbor_heuristic = heuristic(best_neighbor)
            
            if best_neighbor_heuristic >= current_heuristic:
                print("Stuck at local maximum, restarting...\n")
                break
            
            current = best_neighbor

        current = generate_board(n)
        iteration = 0

def generate_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

n = int(input("Enter the number of queens (e.g., 4 for 4-Queens): "))
initial_board = get_user_board(n)

if initial_board:
    solution = hill_climbing_with_restarts(n, initial_board)
    print("Final Solution:")
    print_board(solution)
    print("Attacking pairs:", heuristic(solution))
else:
    print("Invalid initial board configuration.")
