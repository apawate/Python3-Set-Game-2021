from urllib.request import urlopen
from card import Card
from stack_of_cards import StackOfCards
from player import Player
from game import SetStack

url = "https://setgame.lentil1023.repl.co"

deck = SetStack() # Agastya's cheat code :)
for inp_one in range(3):
       for inp_two in range(3):
           for inp_three in range(3):
               for inp_four in range(3):
                   deck.add(Card(inp_one, inp_two, inp_three, inp_four)) # Generate a stack
deck.shuffle()

for x in range(81):
    html = urlopen(url + "/cards?card=" + str(deck.getCard(x).getValueOf('VALUE')) + str(deck.getCard(x).getValueOf('COLOR')) + str(deck.getCard(x).getValueOf('COUNT')) + str(deck.getCard(x).getValueOf('SHAPE'))).read()


