'''
Names: Agastya Pawate and Advaita Guruprasad 

Snapshot #1: Finished everything except playRound(), which is still pending and will hopefully be done by Friday...

Snapshot #2: Finished playRound() and achieved very basic functionality. The next step will be to get the scoring and rounds/games system in, which will require a lot of loops and stuff.

Snapshot #3: Actual functionality is achieved! I think it works fully now. *virtual high five to Advaita*

Snapshot #3a: Okay, now it works for real. The positioning bug deleted the wrong cards when a set was found, but I did some tricky debugging and managed to fix it.

'''
import random
import re
from card import Card
from stack_of_cards import StackOfCards
from player import Player   # Import all the necessary libraries
from urllib.request import urlopen

name = ""

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
    
    def writeToServer(self):
        url = "https://setgame.lentil1023.repl.co"
        urlopen("https://setgame.lentil1023.repl.co/reset")
        for x in range(self.size()):
            html = urlopen(url + "/setup?card=" + str(self.getCard(x).getValueOf('VALUE')) + str(self.getCard(x).getValueOf('COLOR')) + str(self.getCard(x).getValueOf('COUNT')) + str(self.getCard(x).getValueOf('SHAPE'))).read()


cheatStack = SetStack() # Agastya's cheat code :)
for inp_one in range(3):
       for inp_two in range(3):
           for inp_three in range(3):
               for inp_four in range(3):
                   cheatStack.add(Card(inp_one, inp_two, inp_three, inp_four)) # Generate a stack, but don't shuffle it

def buildRealtimeDeck():
    realdeck = SetStack()
    for x in range(81):
        html = urlopen("https://setgame.lentil1023.repl.co/deck").read()
        html = str(html)
        html = html[2:6]
        realdeck.add(Card(int(html[0]), int(html[1]), int(html[2]), int(html[3])))
    return realdeck

def buildUpcards():
    upCards = SetStack()
    length = int(str(urlopen("https://setgame.lentil1023.repl.co/uplen").read())[2:4])
    for x in range(length):
        html = urlopen("https://setgame.lentil1023.repl.co/up").read()
        html = str(html)
        html = html[2:6]
        upCards.add(Card(int(html[0]), int(html[1]), int(html[2]), int(html[3])))
    return upCards

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
  number = pos%(stack.size()//3) + 1 # Determines what the number after the letter is going to be
  reference = letters[letter_indx] + str(number) # Put the reference 
  return reference
  
def converttopos(ref, stack): # Does the opposite of the above function, converts a reference into a position
    mult = 0
    if ref[0] == "b":
        mult = 1
    if ref[0] == "c":
        mult = 2
    pos = mult * (stack.size()//3) + int(ref[1]) - 1
    return pos

# def setInDeck(deck):
  #   check all the possible combinations of 3 cards in this deck until a set is found
def setInDeck(deck):
  for i in range(deck.size()):
    for j in range(deck.size()):
      for k in range(deck.size()):
        check = SetStack()  
        if i == j or j == k or i == k:
          pass
        else:
          check.add(deck.getCard(i))
          check.add(deck.getCard(j))
          check.add(deck.getCard(k))
          if check.isSet():
            print("Your set is: ", check)
            return True
          else:
            continue
  return False
      # Nvm this looks really hard, I'll try and do it on my own time
        #What should i do then
        # Comment the code below, I already did most of it but there is still a bit left to do 
        # Then just try and find bugs in the code, because I'm sure that there are some 
        # I have some feature improvement ideas I'll communicate over hangouts later on, that's when we'll really need to work hard again        


def playRound(deck, upCards, players): # playRound function, the main function that does everything needed for a set game
  score = 0 
  print("A new game has begun!") 
  for x in range(len(players)): # For each player in the "players" list:
    print("Hello, {}!".format(players[x].getName())) # Greet them
  keepPlaying = True 
  cheat = False
  while keepPlaying: 
      currentSet = SetStack() # Clear the current set
      if cheat: # If the cheat code has been entered
          deck = cheatStack # Set the deck to the cheatStack instead of the normal shuffled deck
          upCards = SetStack() # Reset upCards
          for m in range(12):
              upCards.add(deck.deal()) # Deal out the upCards from the new cheat deck
          cheat = False
      upCards.displayInRows() # Display the upCards
      description = input("What is the set (q to exit, n if you can't find it) ? ")

      if description == "n":
        if deck.size() == 0:
            print("No more cards are available.")
        if upCards.size() < 21: # If the deck of cards is less than 21:
            for x in range(3):
                upCards.add(deck.deal()) # Deal three more
        else:
            print("In 21 cards, there's a 100% chance of finding a set. Find a set already!") # Prompt the user to find the set if there are 21 cards
        score -= 1 # Lower the score by 1 every time the user types "n"

      elif deck.size() == 0 and not setInDeck(upCards): # If the size of the deck is zero and there are no sets in the upCards:
          print("Game over!") # End the game
          keepPlaying = False
      
      elif description == "ruheer":
          if setInDeck(upCards):
              print("Yes, there is a set here.")
          else:
              print("No sets were found here.")

      elif description == "q": # If the user wants to quit:
          keepPlaying = False # End the loop
          score = 0 # Reset the score
      elif description == "score": # If "score" keyword is entered
          print("Your score is", score) # Tell the user their score
      elif description == "size": # If "size" keyword is entered
          print("The size of the deck is", deck.size()) # Return the size of the deck (useful for debugging purposes)
      elif description == "asdf": # Cheat code :P
          print("Congratulations.")
          print("Cheat mode has been enabled!")
          cheat = True # Set cheat to True, run above routine
      elif description == "aaa": # Another cheat-ish keyword
          for x in range(upCards.size()):
              upCards.remove(0) # Clear the upCards, allows developers to get to the endgame faster
      else:
        desc_one = description[0:2] # Get the first reference from user
        desc_two = description[3:5] # Get the second reference
        desc_three = description[6:8] # Get the third reference
        describeSet = [desc_one, desc_two, desc_three] # Create a set of descriptions
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
            tobedeleted = []
            for ref in describeSet:
                tobedeleted.append(converttopos(ref, upCards))
            if tobedeleted[1] > tobedeleted[0]:
                tobedeleted[1] = tobedeleted[1] - 1
            if tobedeleted[2] > tobedeleted[0]:
                if tobedeleted[2] > tobedeleted[1]:
                    tobedeleted[2] = tobedeleted[2] - 2
                else:
                    tobedeleted[2] = tobedeleted[2] - 1
            elif tobedeleted[2] > tobedeleted[1]:
                tobedeleted[2] = tobedeleted[2] - 1
            for item in tobedeleted:
                upCards.remove(item)
            if upCards.size() == 9 and deck.size() > 0:
                for b in range(3):
                    upCards.add(deck.deal())
            score = score + 1
        else:
            print("Sorry, that isn't a set.")
            score = score - 1
  return False


def playRealtimeRound(deck, upCards, players): # playRound function, the main function that does everything needed for a set game
  score = 0
  if name == "agastya" or name == "Agastya":
    upCards.writeToServer()
  urlopen("https://setgame.lentil1023.repl.co/init" + "?score=" + str(score) + "&name=" + name)
  print("A new game has begun!") 
  for x in range(len(players)): # For each player in the "players" list:
    print("Hello, {}!".format(players[x].getName())) # Greet them
  keepPlaying = True 
  while keepPlaying: 
      urlopen("https://setgame.lentil1023.repl.co/init" + "?score=" + str(score) + "&name=" + name)
      currentSet = SetStack() # Clear the current set
      upCards = buildUpcards()
      upCards.displayInRows() # Display the upCards
      description = input("What is the set (q to exit, n if you can't find it) ? ")
      status = int(str(urlopen("https://setgame.lentil1023.repl.co/status").read())[2:3])
      urlopen("https://setgame.lentil1023.repl.co/resetstatus")

      if status:
          print("Too late!")
      elif description == "n":
          if deck.size() == 0:
              print("No more cards are available.")
          if upCards.size() < 21: # If the deck of cards is less than 21:
              for x in range(3):
                  upCards.add(deck.deal()) # Deal three more
          else:
              print("In 21 cards, there's a 100% chance of finding a set. Find a set already!") # Prompt the user to find the set if there are 21 cards
          score -= 1 # Lower the score by 1 every time the user types "n"

      elif deck.size() == 0 and not setInDeck(upCards): # If the size of the deck is zero and there are no sets in the upCards:
          print("Game over!") # End the game
          keepPlaying = False
     
      elif description == "ruheer":
          if setInDeck(upCards):
              print("Yes, there is a set here.")
          else:
              print("No sets were found here.")
      
      elif description == "leaderboard":
          for x in range(int(str(urlopen("https://setgame.lentil1023.repl.co/numofplayers").read())[2:3])):
              print(str(urlopen("https://setgame.lentil1023.repl.co/getname").read()), str(urlopen("https://setgame.lentil1023.repl.co/getscore").read()))


      elif description == "q": # If the user wants to quit:
          keepPlaying = False # End the loop
          score = 0 # Reset the score
      elif description == "score": # If "score" keyword is entered
          print("Your score is", score) # Tell the user their score
      elif description == "size": # If "size" keyword is entered
          print("The size of the deck is", deck.size()) # Return the size of the deck (useful for debugging purposes)
      else:
          print(status)
          desc_one = description[0:2] # Get the first reference from user
          desc_two = description[3:5] # Get the second reference
          desc_three = description[6:8] # Get the third reference
          describeSet = [desc_one, desc_two, desc_three] # Create a set of descriptions
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
              tobedeleted = []
              for ref in describeSet:
                  tobedeleted.append(converttopos(ref, upCards))
              if tobedeleted[1] > tobedeleted[0]:
                 tobedeleted[1] = tobedeleted[1] - 1
              if tobedeleted[2] > tobedeleted[0]:
                  if tobedeleted[2] > tobedeleted[1]:
                      tobedeleted[2] = tobedeleted[2] - 2
                  else:
                      tobedeleted[2] = tobedeleted[2] - 1
              elif tobedeleted[2] > tobedeleted[1]:
                  tobedeleted[2] = tobedeleted[2] - 1
              for item in tobedeleted:
                  upCards.remove(item)
              if upCards.size() == 9 and deck.size() > 0:
                  for b in range(3):
                      upCards.add(deck.deal())
              score = score + 1
              urlopen("https://setgame.lentil1023.repl.co/win")
              upCards.writeToServer()
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
        keep_playing = playRealtimeRound(deck, upCards, players)  # repeatedly call playRound until the game is over
   
def play():
    global name
    # get player(s) name
    name = input("What is your name? ")
    player = Player(name)
    players = [player]
    gametype = input("Do you want to play in realtime? (y/n) ")
    # make deck & shuffle it
    cards = SetStack()
    if gametype == "n":
        for inp_one in range(3):
            for inp_two in range(3):
                for inp_three in range(3):
                    for inp_four in range(3):
                        cards.add(Card(inp_one, inp_two, inp_three, inp_four))
        cards.shuffle()
    else:
        cards = buildRealtimeDeck()
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
