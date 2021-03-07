'''
Names: Agastya Pawate and Advaita Guruprasad 

Snapshot #1: Finished everything except playRound(), which is still pending and will hopefully be done by Friday...

Snapshot #2: Finished playRound() and achieved very basic functionality. The next step will be to get the scoring and rounds/games system in, which will require a lot of loops and stuff.

'''
import re
from card import Card
from stack_of_cards import StackOfCards
from player import Player   # Import all the necessary libraries

class SetStack(StackOfCards): # SetStack class which inherits StackOfCards
    def isSet(self): # Is the stack a set?
        #self.size = size
        #self.col 
        c1 = self.getCard(0) # Get first card
        c2 = self.getCard(1) # Get second card
        c3 = self.getCard(2) # Get third card

        if valid(c1.getValueOf('COLOR'), c2.getValueOf('COLOR'), c3.getValueOf('COLOR')) and valid(c1.getValueOf('COUNT'), c2.getValueOf('COUNT'), c3.getValueOf('COUNT')) and valid(c1.getValueOf('SHAPE'), c2.getValueOf('SHAPE'), c3.getValueOf('SHAPE')) and valid(c1.getValueOf('VALUE'), c2.getValueOf('VALUE'), c3.getValueOf('VALUE')) and self.size() == 3: # Tests if the colors, counts, shapes and values all match up per the set game rules (using valid function below)
            return True
        else:
            return False
    def displayInRows(self): # Display in rows, which Advaita wrote and Agastya modified slightly to allow for multiple deck sizes
        titles = ['A', 'B', 'C'] # Row titles
        whereiscard = 0 
        for x in range(1, self.size()//3 + 1): # Agastya added the self.size()//3 + 1 to allow for different deck sizes, this loop prints the column titles 
            print("   ", x, end='    ')
        print() # Newline
        for i in range(3):
            print(titles[i], end=' ') # Print row titles (A, B, C)
            for y in range(self.size()//3): 
                print(self.getCard(whereiscard), end='    ') 
                whereiscard += 1 # Cycle through the deck, adding a card at each position in the grid
            print() # Newline


cheatStack = SetStack() # Agastya's cheat code :)
for inp_one in range(3):
       for inp_two in range(3):
           for inp_three in range(3):
               for inp_four in range(3):
                   cheatStack.add(Card(inp_one, inp_two, inp_three, inp_four)) #Generate a stack, but don't shuffle it

def valid(in_one, in_two, in_three): # Function to determine whether a set of numbers follows the set game rules (used in isSet())
    if in_one == in_two and in_two == in_three: # If the values are equal to each other, return True
        return True
    elif in_one != in_two and in_two != in_three and in_three != in_one: # If all the values are different from each other, return True
        return True
    else:
        return False

# position logic
#    1    2    3    4
# A  0    1    2    3
# B  4    5    6    7
# C  8    9    10   11

def converttoreference(pos, stack): # Converts a number position as listed above (0, 1, 2...) to the (a1, b2, c3...) format
  letters = ["a", "b", "c"] # Possible letters
  letter_indx = pos//(stack.size()//3) # Determines which letter is going to be used, uses the number of cards per row
  number = pos%(stack.size()//3) + 1
  reference = letters[letter_indx] + str(number)
  return reference
  
def converttopos(ref, stack):
    mult = 0
    if ref[0] == "b":
        mult = 1
    if ref[0] == "c":
        mult = 2
    pos = mult * (stack.size()//3) + int(ref[1]) - 1
    return pos


def playRound(deck, upCards, players):
  score = 0 
  print("A new game has begun!") 
  for x in range(len(players)): 
    print("Hello, {}!".format(players[x].getName())) 
  keepPlaying = True
  cheat = False
  while keepPlaying:
      currentSet = SetStack()
      if cheat:
          deck = cheatStack
          upCards = SetStack()
          for m in range(12):
              upCards.add(deck.deal())
          cheat = False
      upCards.displayInRows()
      description = input("What is the set (q to exit, n if you can't find it) ? ")

      if description == "n":
        if upCards.size() < 21:
            for x in range(3):
                upCards.add(deck.deal())
        else:
            print("In 21 cards, there's a 100% chance of finding a set. Find a set already!")
        score -= 1

      elif deck.size() == 0:
          print("Game over!")

      elif description == "q":
          keepPlaying = False
          score = 0
      elif description == "score":
          print("Your score is", score)
      elif description == "size":
          print("The size of the deck is", deck.size())
      elif description == "asdf":
          print("Congratulations.")
          print("Cheat mode has been enabled!")
          cheat = True
      elif description == "aaa":
          for x in range(upCards.size()):
              upCards.remove(0)
      else:
        desc_one = description[0:2]
        desc_two = description[3:5]
        desc_three = description[6:8]
        describeSet = [desc_one, desc_two, desc_three]
        pos = 0
        while pos < upCards.size():
            if (str(describeSet[0]) == converttoreference(pos, upCards)) or (str(describeSet[1]) == converttoreference(pos, upCards)) or (str(describeSet[2]) == converttoreference(pos, upCards)):
                currentSet.add(upCards.getCard(pos))
                pos += 1
            else:
                pos += 1
     
        
      
        if currentSet.isSet():
            print(currentSet, end=" ")
            print("This is a set!")
            for ref in describeSet:
                upCards.remove(converttopos(ref, upCards))
            if upCards.size() == 9 and deck.size() > 0:
                for b in range(3):
                    upCards.add(deck.deal())
            score = score + 1
        else:
            print("Sorry, that isn't a set.")
            score = score - 1
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
        playSetGame(cards, players) # Keep playing games
        choice = input("Do you want to play again? (y/n) ") # Play again?
    return # exit game

def main():
    play() 
    
if __name__ == "__main__":
    main()
