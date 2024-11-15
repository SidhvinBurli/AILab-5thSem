
import random as rd
import math

 
def initial_state(N):
    return [rd.randint(0, N-1) for _ in range(N)]   

 
def cost(s):
    ct = 0
    N = len(s)
    for i in range(N):
        for j in range(i + 1, N):
             
            if s[i] == s[j] or abs(s[i] - s[j]) == j - i:
                ct += 1
    return ct

 
def gen_neighbour(state):
    new_state = state[:]
    col = rd.randint(0, len(state) - 1)
    new_row = rd.randint(0, len(state) - 1)
    new_state[col] = new_row
    return new_state


def sim_ann(N, initial_temp=10000):
    current_state = initial_state(N)
    current_cost = cost(current_state)
    iteration = 0
    while current_cost > 0 and iteration < initial_temp:
        neighbour = gen_neighbour(current_state)
        neighbour_cost = cost(neighbour)
        diff_cost = neighbour_cost - current_cost
        
        if diff_cost <= 0:
            
            current_state = neighbour
            current_cost = neighbour_cost
            
        iteration += 1
        
    return current_state, current_cost

 
def print_sol(state):
    N = len(state)
    board = [['.' for _ in range(N)] for _ in range(N)]
    for col, row in enumerate(state):
        board[row][col] = 'Q'
    for row in board:
        print(' '.join(row))


N = int(input("Enter the number of Queen\n")) 
sol, cost_val = sim_ann(N)

if cost_val == 0:
    print(f"Solution found: {sol}")
    print_sol(sol)  # Print the solution as a matrix if found
else:
    print(f"No solution found. Final cost: {cost_val}")
