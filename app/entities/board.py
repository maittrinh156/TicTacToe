class BoardEntity:
    def __init__(self):
        self.states = [0]*10

    def updateStates(self, position, player):
        self.states[position] = player
        
    def getStates(self):
        return self.states
    
    
        
    