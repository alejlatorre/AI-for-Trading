import cvxpy as cvx
import numpy as np 

def run_cvx():
    x = cvx.Variable(1)                             # Number of variables
    function = (x-1)**2 + 1                         # Function that we want to maximize/minimize
    objective = cvx.Minimize(function)              # Objective
    # quad_form = cvx.quad_form(x, P)               # Represents a quadratic form: (x^T)Px
    # norm_term = cvx.norm(x-b, 2)                  # It creates a norm term: ||x-b||_2
    constraints = [x <= 0]                          # List of constraints
    problem = cvx.Problem(objective, constraints)   # Create the opt. problem object with objective function and constraints
    result = problem.solve()                        # Solver
    print(f'Optimal value of x: {x.value[0]}')      
    print(f'Optimal value of the objective: {problem.value}')
    print(f'Status: {problem.status}')

def test():
    for idx in range(2, 10, 2):
        print(idx)

if __name__ == '__main__':
    run_cvx()
    test()