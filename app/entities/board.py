class BoardEntity:
    def __init__(self):
        self.states = [0]*10
        self.users = None

    def updateStates(self, position, player):
        self.states[position] = player
        
    def getStates(self):
        return self.states
    
    def updateUsers(self, users):
        self.users = users
        
    def getUser(self, id):
        return self.users[id-1]
        
    
    
        
    