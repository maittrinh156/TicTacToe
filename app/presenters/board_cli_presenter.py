from app.interfaces.board_presenter_interface import BoardPresenterInterface
from app.controllers.board_controller import BoardController

class BoardCLIPresenter(BoardPresenterInterface):        
    def showBoard(self, states):
        map = ["_", "O", "X"]
        states = [map[x] for x in states]
        
        print(states[1:4])
        print(states[4:7])
        print(states[7:10])
    
            
    def showWinner(self, win):
        print(f"{win} win!")
        
    def showGameOver(self):
        print("GAME OVER!")  
        
    
        
        
      