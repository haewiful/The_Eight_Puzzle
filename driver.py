from node import Node

def general_search(problem, h_func):
    init_node = Node(problem.init_state, 0)
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
        # print("-queue-")
        # for n in nodes_queue:
        #     print(n)
        # print("-------")
        if problem.goal_test(node.state):
            # print("-final queue-")
            # for n in nodes_queue:
            #     print(n)
            # print("-------")
            return node
        nodes_queue = queueing_function(nodes_queue, expand(node, problem.operator), h_func)

def check_duplicate(checked, state):
    if state in checked:
        return True
    return False

def expand(node, operator):
    return operator.runall(node)

def queueing_function(nodes_queue, expanded, heuristic_func):
    # uniform cost search
    if heuristic_func == None:
        for node in expanded:
            nodes_queue.append(node)
        return nodes_queue
    
    # A* algorithm
    for new_node in expanded: # for each new node
        new_node.heuristic = heuristic_func(new_node.state) # calculate heuristic score
        if len(nodes_queue) == 0:
            nodes_queue.append(new_node)
            continue

        # insert node according to heuristic + depth
        inserted = False
        for i in range(len(nodes_queue)):
            curr_node = nodes_queue[i]

            if curr_node.heuristic+curr_node.depth > new_node.heuristic+new_node.depth:
                nodes_queue.insert(i, new_node) # find the location for the new node
                inserted = True
                break
        if not inserted:
            nodes_queue.append(new_node)
    return nodes_queue

