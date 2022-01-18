# projeto 6: decida por mim, com interface
# faça uma pergunta so software e ele te dará uma resposta
import random
import PySimpleGUI as sg

class DecideForMe:
    def __init__(self):
        self.answers = [
            'sure, you have to do this',
            'idk, you know',
            "don't do this",
            "i think it's the right time"
        ]

    def Initialize(self):
        # layout
        layout = [
            [sg.Text('ask me something: ')],
            [sg.Input()],
            [sg.Output(size=(25,10))],
            [sg.Button('decide for me')]
        ]
        # criar janela
        self.window = sg.Window('Decide For Me!', layout=layout)
        while True:
            # ler valores
            self.events, self.values = self.window.Read()
            # fazer algo com os valores
            if self.events == 'decide for me':
                print(random.choice(self.answers))
                # self.window.Close()

decide = DecideForMe()
decide.Initialize()