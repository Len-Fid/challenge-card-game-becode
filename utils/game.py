from utils.player import Player, Deck

class Board:
    
    def __init__(self, players = [],turn_count = 0,active_cards = [],history_cards = [] ):
        self.players = players
        self.turn_count = 0
        self.active_cards = active_cards
        self.history_cards = history_cards = []

    def start_game(self):
        number_of_players= int(input("Enter the number of players please: "))
        deck = Deck()   
        deck.fill_deck()  # This will fill the deck
        deck.shuffle()
        for i in range(number_of_players):
            player = Player(input("Enter name of the player " + str(i + 1) + ":"))
            self.players.append(player)
        deck.distribute(self.players,player_list)
            # Each turn of the loop is one turn of the game.
        for i in range(0, number_of_cards):
            self.active_cards = []
            for j in self.players:
                card = j.play()
                self.active_cards += [card]
                j.cards.remove(card)
                j.turn_count += 1
            self.history_card += self.active_cards
            self.turn_count += 1
            print(f"Turn number : {self.turn_count} \n Cards played this turn : {self.active_cards}\n Number of cards played in the game : {len(self.history_cards)}")
      
        print("You have no cards left, it's the end !")
       
def __str__(self)-> str:
    return f"Players : {self.players}, turn : {self.turn_count}, cards played this turn : {self.active_cards}, cards played : {self.history_cards}"
