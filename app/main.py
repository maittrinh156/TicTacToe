import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.entities.board import BoardEntity
from app.interactors.board_interactor import BoardInteractor
from app.presenters.board_cli_presenter import BoardCLIPresenter
from app.controllers.board_controller import BoardController

def main():
    
    board = BoardEntity()
    boardPresenter = BoardCLIPresenter()
    boardInteractor = BoardInteractor(board=board, boardPresenter=boardPresenter)
    boardController = BoardController(boardInteractor=boardInteractor)
            
    boardController.playGame()
    
if __name__ == '__main__':
    main()
    
    
    
    