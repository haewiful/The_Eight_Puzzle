def print_puzzle(puzzle):
    print("---------")
    for line in puzzle:
        print("| ", end="")
        for n in line:
            print(n, end=" ")
        print("|")
    print("---------")

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