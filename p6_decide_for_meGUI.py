# projeto 6: decida por mim, com interface
# faça uma pergunta so software e ele te dará uma resposta
import random

class DecideForMe:
    def __init__(self):
        self.answers = [
            'sure, you have to do this',
            'idk, you know',
            "don't do this",
            "i think it's the right time"
        ]

    def Initialize(self):
        input('ask me something: ')
        print(random.choice(self.answers))

decide = DecideForMe()
decide.Initialize()