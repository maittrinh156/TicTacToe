import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.entities.board import BoardEntity
from app.interactors.board_interactor import BoardInteractor
from app.presenters.board_cli_presenter import BoardCLIPresenter

def inputPosition():
    try:
        position = int(input("Please enter the position you want to tick? 1-9 "))
    except ValueError:
        raise Exception("Not a number!")
    
    accepted = [*range(1,10)]
    if position not in accepted:
        raise Exception("Position must be from 1-9 ")
    
    return position


def main():
    
    board = BoardEntity()
    boardPresenter = BoardCLIPresenter()
    boardInteractor = BoardInteractor(board=board, boardPresenter=boardPresenter)

    while not BoardInteractor.isGameOver():
        try:
            position = inputPosition()
            BoardInteractor.tick(position=position)
        except Exception as e:
            print(str(e))
        
if __name__ == '__main__':
    main()
    
    
    
    