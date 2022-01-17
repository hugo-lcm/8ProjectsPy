# simulador de dados com interface
# gera valor de 1 a 6, como um dado comum
import random

class DiceSimulator:
    def __init__(self):
        self.min = 1
        self.max = 6
        self.msg = 'do you like to generate a new value? '

    def Initialize(self):
        ans = input(self.msg)
        try:
            if ans == 'yes' or ans == 'y':
                self.GenerateValue()
            elif ans == 'no' or ans == 'n':
                print('thank you for use our software!')
            else:
                print('please just type "yes" or "no"')
        except:
            print('there was an error receiving your reply')

    def GenerateValue(self):
        print(random.randint(self.min, self.max))

simulator = DiceSimulator()
simulator.Initialize()