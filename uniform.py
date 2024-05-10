class Problem:
    def __init__(self, init):
        self.init_state = init
    
    def goal_test(state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if state == goal:
            return true
        return false

def general_search(problem, queueing_function):
    nodes_queue = make_queue(make_node(problem.initial_state))

    while true:
        if len(nodes_queue) == 0:
            return "failure"
        node = nodes_queue.pop(0)
        if problem.goal_test(node.state):
            return node
        nodes_queue = queueing_function(nodes, expand(node, problem.operators))
