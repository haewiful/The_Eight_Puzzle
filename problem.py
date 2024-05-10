class Problem:
    def __init__(self, init, ope):
        self.init_state = init
        self.operators = ope
    
    def goal_test(self, state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if state == goal:
            return True
        return False

class Operator:
    def runall(self, node):
        left = self.move_blank_left(copy.deepcopy(node))
        # print("left: ", left)
        # print()
        right = self.move_blank_right(copy.deepcopy(node))
        # print("right: ", right)
        # print()
        up = self.move_blank_up(copy.deepcopy(node))
        # print("up: ", up)
        # print()
        down = self.move_blank_down(copy.deepcopy(node))
        # print("down: ", down)
        # print()

        expanded = []
        if left != None:
            expanded.append(left)
        if right != None:
            expanded.append(right)
        if up != None:
            expanded.append(up)
        if down != None:
            expanded.append(down)
        
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

    def move_blank_right(self, node):
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    if j<2:
                        node[i][j] = node[i][j+1]
                        node[i][j+1] = 0
                        return node
        return None

    def move_blank_down(self, node):
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    if j<2:
                        node[i][j] = node[i+1][j]
                        node[i+1][j] = 0
                        return node
        return None

    def move_blank_up(self, node):
        for i in range(3):
            for j in range(3):
                if node[i][j] == 0:
                    if i>0:
                        node[i][j] = node[i-1][j]
                        node[i-1][j] = 0
                        return node
        return None