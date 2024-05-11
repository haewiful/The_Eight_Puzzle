class Problem:
    def __init__(self, init, operator):
        self.init_state = init
        self.operator = operator
    
    def goal_test(self, state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if state == goal:
            return True
        return False