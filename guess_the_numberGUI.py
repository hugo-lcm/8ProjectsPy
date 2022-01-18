# projeto 4: adivinhe o número, com interface
# criar um algoritmo que gere um valor aleatório que o usuário tem que tentar adivinhar
import random
import PySimpleGUI as sg


class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.min = 1
        self.max = 12
        self.try_again = True
    

    def Initialize(self):
        # layout
        layout = [
            [sg.Text('your guess', size=(20,0))],
            [sg.Input(size=(18,0), key ='AttemptValue')],
            [sg.Button(('Try!'))],
            [sg.Output(size=(20,10))]
        ]
        # criar janela
        self.window = sg.Window('guess the number!', layout=layout)
        self.GenerateRandomValue()
        try:
            while True:
                # receber valores
                self.event, self.values = self.window.Read()
                # fazer algo com esses valores 
                if self.event == 'Try!':
                    self.attempt_value = self.values['AttemptValue']
                    while self.try_again == True:
                        if int(self.attempt_value) > self.random_value:
                            print('try a lower value')
                            #self.RedScreenValues()
                            break
                        elif int(self.attempt_value) < self.random_value:
                            print('try a higher value')
                            #self.ReadScreenValues()
                            break
                        if int(self.attempt_value) == self.random_value:
                            self.try_again = False
                            print(f'congrats, {self.attempt_value} is the correct number')
        except:
            print('type just numbers, please!')
            self.Initialize()


    def GenerateRandomValue(self):
        self.random_value = random.randint(self.min, self.max)


gtn = GuessTheNumber()
gtn.Initialize()