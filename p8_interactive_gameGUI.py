# project 8: adventure game, with interface
# decision game in which they will interfere at the end of the game

# scenario: the character is in a war between two nations (side A, side B), only side A will win, decisions made by the character have to 
# lead side A to victory in order to win the game.
import PySimpleGUI as sg

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
        # layout
        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0), key='choice')],
            [sg.Button('start'), sg.Button('respond')]
        ] 
        # create Window
        self.window = sg.Window('adventure game', layout=layout)
        while True:
            # read datas
            self.ReadValues()
            # do something with the datas
            if self.event == 'start':
                print(self.question1)
                self.ReadValues()
                if self.values['choice'] == 'n':
                    print(self.question2)
                    self.ReadValues()
                    if self.values['choice'] == 'sword':
                        print(self.final1)
                    if self.values['choice'] == 'shield':
                        print(self.final2)
                if self.values['choice'] == 's':
                    print(self.question3)
                    self.ReadValues()            
                    if self.values['choice'] == 'frontline':
                        print(self.final3)
                    if self.values['choice'] == 'tactical':
                        print(self.final4)


    def ReadValues(self):
        self.event, self.values = self.window.Read()


game = AdventureGame()
game.Initialize()