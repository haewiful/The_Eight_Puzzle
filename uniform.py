import copy

from problem import Problem
from eight_puzzle_operator import Operator
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

# def uniform_cost(nodes_queue, expanded, _):
#     for node in expanded:
#         nodes_queue.append(node)
#     return nodes_queue

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

def calculate_misplaced_tiles(state):
    answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    count=0
    for i in range(3):
        for j in range(3):
            if answer[i][j] != state[i][j]:
                count+=1
    if count > 0:
        count -= 1 # because we don't count the blank being misplaced
    return count

def calculate_mahattan_distance(state):
    answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    count=0
    # print("calculate for", state)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0: # don't count the distance for blank
                continue
            if answer[i][j] != state[i][j]:
                for x in range(3):
                    for y in range(3):
                        if state[i][j] == answer[x][y]:
                            # print("for num", state[i][j], "distance is", abs(i-x)+abs(j-y))
                            count += abs(i-x)+abs(j-y)
                            break
    # print("score is", count)
    return count

def print_puzzle(puzzle):
    print("---------")
    for line in puzzle:
        print("| ", end="")
        for n in line:
            print(n, end=" ")
        print("|")
    print("---------")

def main(algorithm, puzzle):
    match algorithm:
        case 1: # Uniform Cost Search
            print("You chose Uniform Cost Search")
            problem = Problem(puzzle, Operator())
            node = general_search(problem, None)

        case 2: # A* with Misplaced Tile heuristic
            print("You chose A* with Misplaced Tiles heuristic")
            problem = Problem(puzzle, Operator())
            node = general_search(problem, calculate_misplaced_tiles)

        case 3: # A* with Manhattan Distance heuristic
            print("You chose A* with Manhattan Distance heuristic")
            problem = Problem(puzzle, Operator())
            node = general_search(problem, calculate_mahattan_distance)


    if isinstance(node, str):
        print(node)
        return
    print("---goal acheived---")
    print(node)
    print("It took", node.depth, "moves")

# test cases
test = []

test.append([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]])

test.append([[1, 2, 3],
             [4, 5, 6],
             [0, 7, 8]])

test.append([[1, 2, 3],
             [5, 0, 6],
             [4, 7, 8]])

test.append([[1, 3, 6],
             [5, 0, 2],
             [4, 7, 8]])

test.append([[1, 3, 6],
             [5, 0, 7],
             [4, 8, 2]])

test.append([[1, 6, 7],
             [5, 0, 3],
             [4, 8, 2]])

test.append([[7, 1, 2],
             [4, 8, 5],
             [6, 3, 0]])

test.append([[0, 7, 2],
             [4, 6, 1],
             [3, 5, 8]])



while True:
    print('\nThis is "The Eight Puzzle Solver". Please enter your choice from the menu.')
    print("\n---Menu---")
    print(" 1 > Run with provided test cases")
    print(" 2 > Run with customized puzzle")
    print("-1 > Quit")
    menu = int(input("Enter a number > "))
    puzzle = None

    match menu:
        case 1: # use test cases
            print("\nYou chose to run with provided test cases.")
            print("Please choose which test case you want to run.")
            for i in range(8):
                print(str(i) + ".")
                print_puzzle(test[i])
                print()
            choice = int(input("Enter a number > "))
            if choice < 0 or choice > 7:
                print("[Invalid Input]")
                continue
            puzzle = copy.deepcopy(test[choice])
        
        case 2: # use custom puzzle
            print("\nYou chose to create your own puzzle. ")
            print("Enter problem in the following format")
            print("-------\n|1 2 3|\n|4 5 6|\n|7 8 9|\n-------")

            init = []
            for i in range(3):
                tmp = input().split()
                tmp = list(map(lambda x: int(x), tmp))
                init.append(tmp)

            if not check_input(init):
                print("Invalid input")
                continue
            print()

            puzzle = init
        
        case _: # quit solver
            break

    # choose algorithm to run with
    print("\nWe have 3 search algorithms you can choose from. Please choose one")
    print("1 > Uniform Cost Search")
    print("2 > A* with Misplaced Tiles heuristic")
    print("3 > A* with Manhattan Distance heuristic")
    algorithm = int(input("Enter a number > "))
    print()

    if algorithm < 1 or algorithm > 3:
        print("Invalid input")
        continue

    main(algorithm, puzzle)
