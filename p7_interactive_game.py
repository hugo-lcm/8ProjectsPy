# project 7: adventure game
# decision game in which they will interfere at the end of the game

# scenario: the character is in a war between two nations (side A, side B), only side A will win, decisions made by the character have to 
# lead side A to victory in order to win the game.

class AdventureGame:
    def __init__(self):
        self.question1 = 'were you born, in the north or south?' # north = side A, south = side B
        self.question2 = 'do you prefer sword or shield?' # sword = side A, shield = side B
        self.question3 = 'what is your specialty?' # frontline = side A, tactical = side B

    
    def Initialize(self):


game = AdventureGame()
game.Initialize()

# https://youtu.be/7U3-pJZkN-o?t=6895