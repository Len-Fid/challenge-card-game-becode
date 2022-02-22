import sys
sys.path.append(r'C:\Users\Fidrmuc\Desktop\COMP167\challenge-card-game-becode')
from card import Card
from random import choice

class Player:

    def __init__ (self, name:str, cards=[], number_of_cards:int = 0, history=[], turn_count: int = 0):   
        self.name = name
        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    
    def play(self):    
        chosenCard = choice(self.cards)
        self.turn_count += 1
        self.history.append (chosenCard)
        print (self.name, self.turn_count, "played: ", chosenCard)
        return chosenCard
        
    def __str__(self) -> str:
        return self.name + " has " + str(len(self.cards)) + " cards."

""" test = Player("Lena")
test.cards.append (Card("red", "♥", "Q"))
test.play () """

from random import shuffle

class Deck:
    def __init__ (self):
        self.cards = []

    def fill_deck (self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        icons = ["♥", "♦", "♣", "♠"]
        for i in range(0, 4):
            if i in ["♥", "♦"]:
                color = "red"
            else:
                color = "black"
                for v in range(0, 13):
                    self.cards.append(Card(values[v], icons[i]))

    def shuffle (self):
        shuffle(self.cards)

    def distribute (self, n_players):
        number_of_cards = int(52 / len(n_players))
        for i in n_players:
            for j in range(0, number_of_cards):
                i.cards += [self.cards[0]]
                self.cards.pop(self.cards[0])

    def __str__(self) -> str:
        message = ""
        for card in self.cards:
            message += card + "\n"
        return message
    
