# projeto 2: simulador de dados com interface
# gera valor de 1 a 6, como um dado comum
import random
import PySimpleGUI as sg

class DiceSimulator: 
    def __init__(self):
        self.min = 1
        self.max = 6
        self.msg = 'do you like to generate a new value? '
        # layout
        self.layout = [
            [sg.Text('play the dice? ')],
            [sg.Button('yes'), sg.Button('no')]
        ]


    def Initialize(self):
         # window
        self.window = sg.Window('dice simulator',layout=self.layout)
        # read values
        self.events, self.values = self.window.Read()
        # do something with values
        try:
            if self.events == 'yes' or self.events == 'y':
                self.GenerateValue()
            elif self.events == 'no' or self.events == 'n':
                print('thank you for use our software!')
            else:
                print('please just type "yes" or "no"')
        except:
                print('there was an error receiving your reply')

    def GenerateValue(self):
        print(random.randint(self.min, self.max))

simulator = DiceSimulator()
simulator.Initialize()