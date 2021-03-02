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
    def isSet(self):
        #self.size = size
        #self.col 
        c1 = self.getCard(0)
        c2 = self.getCard(1)
        c3 = self.getCard(2)
        if valid(c1.getValueOf('COLOR'), c2.getValueOf('COLOR'), c3.getValueOf('COLOR')) and valid(c1.getValueOf('COUNT'), c2.getValueOf('COUNT'), c3.getValueOf('COUNT')) and valid(c1.getValueOf('SHAPE'), c2.getValueOf('SHAPE'), c3.getValueOf('SHAPE')) and valid(c1.getValueOf('VALUE'), c2.getValueOf('VALUE'), c3.getValueOf('VALUE')) and self.size() == 3:
            return True
        else:
            return False
    def displayInRows(self):
        titles = ['A', 'B', 'C']
        for x in range(4):
            print("   ", x, end='    ')
        print()
        for i in range(3):
            print(titles[i], end=' ')
            for y in range(4):
                print(self.deal(), end='    ')
            print()

    
# Input:
#   deck - SetStack which is the deck to draw new cards from
#   upCards - SetStack that are face up
#   players - list of Player
# Return boolean: True to continue game, False to end game

def valid(in_one, in_two, in_three):
    if in_one == in_two and in_two == in_three:
        return True
    elif in_one != in_two and in_two != in_three and in_three != in_one:
        return True
    else:
        return False



def playRound(deck, upCards, players):
    upCards.displayInRows()
    
    return False

# Input:
#   deck - SetStack which is the deck to draw new cards from
#   players - list of Player
# No return value
def playSetGame(deck, players):
    upCards = SetStack()
    keep_playing = True
    for i in range(12):
        upCards.add(deck.deal()) # deal 12 cards from the deck
    while keep_playing:
        keep_playing = playRound(deck, upCards, players)  # repeatedly call playRound until the game is over
   
def play():
    # get player(s) name
    name = input("What is your name? ")
    player = Player(name)
    players = [player]
    # make deck & shuffle it
    cards = SetStack()
    for inp_one in range(3):
        for inp_two in range(3):
            for inp_three in range(3):
                for inp_four in range(3):
                    cards.add(Card(inp_one, inp_two, inp_three, inp_four))
    cards.shuffle()
    playSetGame(cards, players) # call playSetGame
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
    print(deck.isSet())			# should print True
    #deck.displayInRows()


    player = Player("Mark") 		# make a player called Mark
    players = [ player ]
    play() 
    
if __name__ == "__main__":
    main()
