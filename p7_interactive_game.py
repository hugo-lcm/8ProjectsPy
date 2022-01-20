# project 7: adventure game
# decision game in which they will interfere at the end of the game

# scenario: the character is in a war between two nations (side A, side B), only side A will win, decisions made by the character have to 
# lead side A to victory in order to win the game.

class AdventureGame:
    def __init__(self):
        self.question1 = 'were you born, in the north or south? (n/s) ' # north = side A, south = side B
        self.question2 = 'do you prefer sword or shield? (sword/shield) ' # sword = side A, shield = side B
        self.question3 = 'what is your specialty? (frontline/tactical) ' # frontline = side A, tactical = side B
        self.final1 = 'you will be a hero on the front lines!'
        self.final2 = 'you will be a hero protecting our troops!'
        self.final3 = 'you will sacrifice yourself in battle!'
        self.final4 = 'you are not able to fight this battle!'

    
    def Initialize(self):
        a1 = input(self.question1)
        if a1 == 'n':
            a1b = input(self.question2)
            if a1b == 'sword':
                print(self.final1)
            if a1b == 'shield':
                print(self.final2)
        if a1 == 's':
            a1b = input(self.question3)            
            if a1b == 'frontline':
                print(self.final3)
            if a1b == 'tactical':
                print(self.final4)


game = AdventureGame()
game.Initialize()

# https://youtu.be/7U3-pJZkN-o?t=6895