import copy

from problem import Problem
from eight_puzzle_operator import Operator
from node import Node

def general_search(problem, queueing_function):
    init_node = Node(problem.init_state)
    nodes_queue = [init_node] # make queue with initial state
    checked = []

    while True:
        if len(nodes_queue) == 0:
            return "failure"
        node = nodes_queue.pop(0)
        if(check_duplicate(checked, node.state)):
            continue
        checked.append(node.state)
        print(node)
        if problem.goal_test(node.state):
            return node
        nodes_queue = queueing_function(nodes_queue, expand(node, problem.operators))

def check_duplicate(checked, state):
    if state in checked:
        return True
    return False

def expand(node, operators):
    return operators.runall(node)

def check_input(state):
    if len(state) != 3:
        return False
    for line in state:
        if len(line) != 3:
            return False
        for x in line:
            if not isinstance(x, int):
                return False
    
    return True

def uniform_cost(nodes_queue, expanded):
    for node in expanded:
        nodes_queue.append(node)
        
    return nodes_queue

def main():
    init = []
    print("Enter problem in the following format")
    print("-------\n|1 2 3|\n|4 5 6|\n|7 8 9|\n-------")
    for i in range(3):
        tmp = input().split()
        tmp = list(map(lambda x: int(x), tmp))
        init.append(tmp)

    if not check_input(init):
        print("Invalid input")
        return

    problem = Problem(init, Operator())
    print()
    node = general_search(problem, uniform_cost)
    print("---goal acheived---")
    print(node)
    print("It took", node.depth, "moves")

main()
