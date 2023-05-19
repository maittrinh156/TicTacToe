class BoardController:
    def __init__(self, boardInteractor):
        self.boardInteractor = boardInteractor
        
    def handleUserInput(self, id):
        user = input(f"Please input the user {id+1}: ")
        if user == "":
            raise Exception("Invalid user!")
        return user
            
    def handleMultipleUsersInput(self):
        users = []
        id = 0
        while id < 2:
            try:
                users.append(self.handleUserInput(id))
            except Exception as e:
                id -= 1
                print(e)
            id += 1
        return users
        
    def handlePositionInput(self):
        try:
            position = int(input("Please enter the position you want to tick? 1-9 "))
        except ValueError:
            raise Exception("Not a number!")
        
        accepted = [*range(1,10)]
        if position not in accepted:
            raise Exception("Position must be from 1-9 ")
        
        return position
        
    def playGame(self):
        
        users = self.handleMultipleUsersInput()
        self.boardInteractor.addUsers(users)
        
        while not self.boardInteractor.isGameOver():
            try:
                position = self.handlePositionInput()
                self.boardInteractor.tick(position=position)
            except Exception as e:
                print(str(e))
