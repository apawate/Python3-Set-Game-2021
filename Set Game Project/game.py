'''
Names: Agastya Pawate and Advaita Guruprasad 

Snapshot #1: Finished all the 3 classes and tested them out and they
seem to work...???

'''
import re
from card import Card
from stack_of_cards import StackOfCards
from player import Player

class SetStack(StackOfCards):
    pass
    
# Input:
#   deck - SetStack which is the deck to draw new cards from
#   upCards - SetStack that are face up
#   players - list of Player
# Return boolean: True to continue game, False to end game
def playRound(deck, upCards, players):
    pass

# Input:
#   deck - SetStack which is the deck to draw new cards from
#   players - list of Player
# No return value
def playSetGame(deck, players):
    # deal 12 cards from the deck
    # repeatedly call playRound until the game is over
    pass
   
def play():
    # get player(s) name
    name = input("What is your name? ")
    # make deck & shuffle it
    cards = SetStack()
    cards.shuffle()
    playSetGame(cards, name) # call playSetGame
    choice = input("Do you want to play again? (y/n) ") # Play again? (first time around)
    while choice == 'y': # While the choice is yes (also catches the "n" like an if statement)
        playSetGame(cards, name) # Keep playing games
        choice = input("Do you want to play again? (y/n) ") # Play again?
    return # exit game

def main():
    # sample code using Card, StackOfCards, Player classes
    c = Card(0, 1, 2, 0)				# make a Set card with attributes of
							# value: 0
							# color: 1
							# count: 2
							# shape: 0
    print(c)						# will print out x x x

    deck = SetStack()  				# make a stack of cards
    deck.add(c)						# add the card to the deck
    deck.add(Card(1, 2, 2, 2))		# add another card to the deck
    deck.add(Card(2, 0, 2, 1))		# add another card to the deck
    print(deck)						# should print three cards
    #print(deck.isSet())			# should print True
    #deck.displayInRows()


    player = Player("Mark") 		# make a player called Mark
    players = [ player ]
    play() 
    playSetGame(deck, players)
    
if __name__ == "__main__":
    main()
