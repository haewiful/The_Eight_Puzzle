import copy

from problem import Problem
from eight_puzzle_operator import Operator

def general_search(problem, queueing_function):
    nodes_queue = [problem.init_state] # make queue with initial state

    while True:
        if len(nodes_queue) == 0:
            return "failure"
        node = nodes_queue.pop(0)
        if problem.goal_test(node):
            return node
        nodes_queue = queueing_function(nodes, expand(node, problem.operators))

def expand(node, operators):
    return operators.runall(node)

def uniform_cost(nodes, expanded):
    pass

# l = "1 2 3"
# n = map(lambda x: int(x), l.split())
# print(list(n))

init = []
print("Enter problem in the following format")
print("-------\n|1 2 3|\n|4 5 6|\n|7 8 9|\n-------")
for i in range(3):
    tmp = input().split()
    tmp = list(map(lambda x: int(x), tmp))
    init.append(tmp)

# for node in expand(init, Operator()):
#     for line in node:
#         print(line)
#     print()



problem = Problem(init, Operator())
print(problem.init_state)
# print(general_search(problem, None))
