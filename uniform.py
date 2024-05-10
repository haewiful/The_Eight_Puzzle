import copy



class Problem:
    def __init__(self, init):
        self.init_state = init
    
    def goal_test(state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if state == goal:
            return true
        return false

class Operator:
    def runall(self, node):
        left = self.move_blank_left(copy.deepcopy(node))
        print("left: ", left)

        expanded = []
        if left != None:
            expanded.append(left)
        
        return expanded

    def move_blank_left(self, node):
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    if j>0:
                        node[i][j] = node[i][j-1]
                        node[i][j-1] = 0
                        return node
        return None

def general_search(problem, queueing_function):
    nodes_queue = [problem.initial_state] # make queue with initial state

    while true:
        if len(nodes_queue) == 0:
            return "failure"
        node = nodes_queue.pop(0)
        if problem.goal_test(node.state):
            return node
        nodes_queue = queueing_function(nodes, expand(node, problem.operators))

def expand(node, operators):
    return operators.runall(node)

# def uniform_cost(nodes, k):

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

print(expand(init, Operator()))


# problem = Problem(init)
# print(problem.init_state)