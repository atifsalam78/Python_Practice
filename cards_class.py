"""
###Q-2: Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

    The Deck class should have a deal method to deal a single card from the deck
    After a card is dealt, it is removed from the deck.
    There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
    The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

Deck Class

    It is class of all possible cards in a deck. Total 52 cards.
    Methods - deal() it will take out one card from the deck of cards.
    Deck of cards should get shuffeled while creating the deck object.
    no of cards remaining in deck - <number> should dsiplay on printing any deck object.

Card class

    It is a class of card
    Atrributes - suit and value
    <suit> of <value> should dsiplay on printing any card object.
"""
import random
class Deck_of_Cards:    
    
    def __init__(self): 
        self.shuffle()        
        
    def deal(self, card):        
        del self.deck[card.suit][Card.card_index]        
    
    def shuffle(self):
        deck_suit = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        deck_value = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        random.shuffle(deck_suit)        
        self.deck = {deck_suit[0]: random.sample(deck_value,13), deck_suit[1]: random.sample(deck_value,13),
                     deck_suit[2]: random.sample(deck_value,13), deck_suit[3]: random.sample(deck_value,13)}        
        
    def __str__(self):
        return "No. of cards remaining in deck - <{}>".format(len(self.deck["Hearts"])+len(self.deck["Diamonds"])
                                                              +len(self.deck["Clubs"])+len(self.deck["Spades"]))
    
class Card:
    
    card_index = None
    
    def __init__(self, deck):
        self.deck = deck       
        Card.card_index = random.randint(0,12)
        self.suit = random.choice(list(self.deck))
        self.value = self.deck[self.suit][Card.card_index]
          
    def __str__(self):
        return "<{}> of <{}>".format(self.suit, self.value)
    
deck1 = Deck_of_Cards()
card1 = Card(deck1.deck)
print(card1)
deck1.deal(card1)
print(deck1)