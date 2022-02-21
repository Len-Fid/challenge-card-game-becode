class Symbol:
    color = ["red","black"]
    icon =  ["♥","♦","♣","♠"]
    
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon
    
    def __str__ (self):
        return f"{self.color} {self.icon}"
    
class Card(Symbol): # inherits from Symbol
    value = ["A","2", "3","4", 
           "5", "6", "7",
           "8", "9", "10",
           "J", "Q","K"]
 
    def __init__(self, color, icon,value):
        super().__init__(color, icon)
        self.value = value

    def __str__ (self):
        return f"{self.color} {self.icon} {self.value}"

my_card = Card ("red","♦","Q")
print (my_card)