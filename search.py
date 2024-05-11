import copy

from problem import Problem
from eight_puzzle_operator import Operator
from node import Node
from utils import test, print_puzzle, check_input
from driver import general_search

def main():
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
                    print("[Invalid input]")
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
            print("[Invalid input]")
            continue

        execute_search(algorithm, puzzle)

def execute_search(algorithm, puzzle):
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
    print("--- Solved ---")
    print_puzzle(puzzle)
    print("=> It took", node.depth, "moves to solve this puzzle.")

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
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0: # don't count the distance for blank
                continue
            if answer[i][j] != state[i][j]:
                for x in range(3):
                    for y in range(3):
                        if state[i][j] == answer[x][y]:
                            count += abs(i-x)+abs(j-y)
                            break
    return count


main()