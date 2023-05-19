from app.entities.board import BoardEntity
from app.interfaces.board_presenter_interface import BoardPresenterInterface

class BoardInteractor:
    def __init__(self, board: BoardEntity, boardPresenter: BoardPresenterInterface):
        self.board = board
        self.boardPresenter = boardPresenter
        
    def calculateNextPlayer(self):
        states = self.board.getStates()
        counts = [states.count(x) for x in range(3)]
        if counts[1] > counts[2]:
            return 2
        return 1
        
    def checkWin(self):
        states = self.board.getStates()
        
        lines = [states[1::4], states[3:8:2]]
        
        for i in range(1, 4):
            lines.append(states[i:i+3])
            lines.append(states[i::3])
            
        for line in lines:
            if len(set(line)) == 1 and line[0] != 0:
                return line[0]
        
        return 0
    
    def isValidity(self, position):
        states = self.board.getStates()
        
        if states[position] != 0:
            return False
        
        return True
    
    def isGameOver(self):
        if self.checkWin():
            return True
        
        states = self.board.getStates()
        if states.count(0) <= 1:
            return True
        
        return False
    
    def tick(self, position):
        if not self.isValidity(position=position):
            raise Exception("Position not valid!")
        player = self.calculateNextPlayer()
        
        self.board.updateStates(player=player, position=position)
        
        self.boardPresenter.showBoard(self.board.getStates())
        
        win = self.checkWin()
        
        if win != 0:
            self.boardPresenter.showWinner(self.board.getUser(win))            
        elif self.isGameOver():
            self.boardPresenter.showGameOver()
            
    def addUsers(self, users):
        self.board.updateUsers(users)
            
            
            
            
        
    
    