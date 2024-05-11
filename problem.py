class Problem:
    def __init__(self, init, operator, heuristic_func=None):
        self.init_state = init
        self.operator = operator
        self.h_func = heuristic_func
    
    def goal_test(self, state):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if state == goal:
            return True
        return False