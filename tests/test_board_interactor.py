import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.interactors.board_interactor import BoardInteractor
from app.interfaces.board_presenter_interface import BoardPresenterInterface

class MockBoardEntity:
    def __init__(self):
        self.states = [0, 0, 0, 1, 2, 0, 2, 0, 1, 0]
        
    def getStates(self):
        return self.states
    
    def updateStates(self, player, position):
        self.states[2] = 1

class MockBoardPresenter(BoardPresenterInterface):
    def showWinner(self, win):
        print(f"{win} Win!")
        
    def showBoard(self, states):
        print(f"Board: {states}")
                
    def showGameOver(self):
        print("Game over!")
        
class TestBoardInteractor:
    def __init__(self):
        self.boardEntity = MockBoardEntity()
        self.boardPresenter = MockBoardPresenter()
        self.boardInteractor = BoardInteractor(board=self.boardEntity, boardPresenter=self.boardPresenter)
    
    def testCalculateNextPlayer(self):
        assert self.boardInteractor.calculateNextPlayer() == 1
        
    def testCheckWin(self):
        assert self.boardInteractor.checkWin() == 0
        
    def testIsValidity(self):
        assert self.boardInteractor.isValidity(3) is False
        
    def testIsGameOver(self):
        assert self.boardInteractor.isGameOver() is False
        
    def testTick(self):
        self.boardInteractor.tick(2)
        states = self.boardEntity.getStates()
        assert states == [0, 0, 1, 1, 2, 0, 2, 0, 1, 0]
        
        
        
        
        
        
        