class Node:
    def __init__(self, init, g=0, h=0):
        self.state = init
        self.depth = g
        self.heuristic = h
    
    def __str__(self):
        if self.state == None:
            print("[ERROR] not initialized")
        node_str = ""
        for line in self.state:
            for n in line:
                node_str += str(n) + " "
            node_str += "\n"
        
        if self.depth != 0:
            node_str += "g(n)= " + str(self.depth) + "\n"
        if self.heuristic != 0:
            node_str += "h(n)= " + str(self.heuristic) + "\n"
        return node_str