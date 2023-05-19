from abc import ABC, abstractclassmethod

class BoardPresenterInterface(ABC):
    @abstractclassmethod
    def showWinner():
        pass
    
    @abstractclassmethod
    def showBoard():
        pass
    
    @abstractclassmethod
    def showGameOver():
        pass