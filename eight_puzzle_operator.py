from node import Node
import copy

class Operator:

    def runall(self, node):
        # left
        left_state = self.move_blank_left(copy.deepcopy(node.state))
        left = Node(left_state, node.depth+1, 0)
        # right
        right_state = self.move_blank_right(copy.deepcopy(node.state))
        right = Node(right_state, node.depth+1, 0)
        # up
        up_state = self.move_blank_up(copy.deepcopy(node.state))
        up = Node(up_state, node.depth+1,0)
        # down
        down_state = self.move_blank_down(copy.deepcopy(node.state))
        down = Node(down_state, node.depth+1, 0)

        expanded = []
        if left_state != None:
            expanded.append(left)
        if right_state != None:
            expanded.append(right)
        if up_state != None:
            expanded.append(up)
        if down_state != None:
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
                    if i<2:
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