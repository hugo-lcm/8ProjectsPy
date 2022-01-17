# projeto 3: adivinhe o número
# criar um algoritmo que gere um valor aleatório que o usuário tem que tentar adivinhar
import random

class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.min = 1
        self.max = 100
        self.try_again = True
    
    def Initialize(self):
        self.GenerateRandomValue()
        self.NewAtt()
        try:
            while self.try_again:
                if self.att > self.random_value:
                    print('try a lower value')
                    self.NewAtt()
                elif self.att < self.random_value:
                    print('try a higher value')
                    self.NewAtt()
                else:
                    print(f'congrants, {self.att} is the correct number!')
                    self.try_again = False
        except:
            print('type just numbers, please!')
            self.Initialize()

    
    def NewAtt(self):
        self.att = int(input('guess the number: '))
        

    def GenerateRandomValue(self):
        self.random_value = random.randint(self.min, self.max)

gtn = GuessTheNumber()
gtn.Initialize()

# https://www.youtube.com/watch?v=7U3-pJZkN-o&ab_channel=DevAprender 54min