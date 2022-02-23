import sys
sys.path.append(r'C:\Users\Fidrmuc\Desktop\COMP167\challenge-card-game-becode\utils')
from card import Card
from random import choice

class Player:

    def __init__ (self, name:str, hand=[], number_of_cards:int = 0, history=[], turn_count: int = 0):   
        self.name = name
        self.hand = hand
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    
    def play(self):    
        chosenCard = choice(self.player_cards)
        self.turn_count += 1
        self.number_of_cards -= 1
        self.history.append (chosenCard)
        return chosenCard
        
    def __str__(self) -> str:
        print(f"Player {self.name} turn count:{self.turn_count} played card:{chosenCard}")

""" test = Player("Lena")
test.cards.append (Card("red", "♥", "Q"))
test.play () """

from random import shuffle

class Deck:
    def __init__ (self):
        self.cards = []
        self.hand =[]
                    
    def fill_deck(self):
        for i in Card.icon:
            if i in ["♥", "♦"]:
                color = "red"
            else:
                color = "black"
                for v in Card.value:
                    self.cards.append(v+i)

    def shuffle (self):
        shuffle(self.cards)

 
    def distribute (self, n_players,player):
            number_of_cards = int(52 // n_players)
            for each in player:
                each.hand += self.cards[0:number_of_cards]
                del self.cards[0:number_of_cards]



    def __str__(self) -> str:
        return f"Cards in deck : {self.cards}"
