from flask import Flask, request
app = Flask('app')

scores = []
names = []
cards = []
upcards = []

firstname = ""

firstgotten = False

index = -1
updex = -1
scoredex = -1
namedex = -1

won = "0"


@app.route('/deck')
def returndeck():
  global index
  global cards
  print(cards)
  print(index)
  index = index + 1
  if index == len(cards) - 1:
    index = 0
  return cards[index]

@app.route('/deal')
def deal():
  return cards.pop(0)
  
@app.route('/clear')
def clear():
  global scores
  global names
  scores = []
  names = []
  return "cleared"

@app.route('/init')
def makescore():
  global scores
  global names
  global firstgotten
  global firstname
  score = request.args['score']
  name = request.args['name']
  scores.append(score)
  names.append(name)
  if not firstgotten:
      firstname = name
      firstgotten = True
  return "hi"

#@app.route('/getscore')
#def getsc():
  #global scores
  #global scoredex
  #scoredex = scoredex + 1
  #if scoredex == len(scores)-1:
  #  scoredex = 0
  #return scores[scoredex]

@app.route('/')
def getld():
  global names
  global scores
  bigstring =  ""
  for indx in range(len(names)):
    bigstring = bigstring + "\n" + "    Name: " + names[indx] + "  Score: " + scores[indx]

  return bigstring

@app.route('/numofplayers')
def numofplayers():
  global names
  return str(len(names))

@app.route('/decksize')
def getsize():
  global cards
  global index
  index = -1
  return str(len(cards))

@app.route('/cards')
def makedeck():
  card = request.args['card']
  cards.append(card)
  return str(cards)

@app.route('/score')
def getscore():
  return scores.pop()

@app.route('/status')
def getstatus():
  global won
  return won

@app.route('/resetstatus')
def resetstatus():
  global won
  won = "0"
  return "resetted"

@app.route('/win')
def somewon():
  global won
  won = "1"
  return ("someone won!")

@app.route('/up')
def getcards():
  global upcards
  global updex
  print(upcards)
  print(updex)
  updex = updex + 1
  if updex == len(upcards):
    updex = 0
  return upcards[updex]

@app.route('/reset')
def reset():
  global upcards
  upcards = []
  return "resetted"

@app.route('/uplen')
def getlen():
  global updex
  updex = -1
  return str(len(upcards))

@app.route('/setup')
def setup():
  upcard = request.args['card']
  upcards.append(upcard)
  return str(upcards)

@app.route('/cleardeck')
def cleardeck():
  global cards
  cards = []
  return "cleared"

@app.route('/first')
def first():
    global firstname
    return firstname

app.run(host='0.0.0.0', port=8080)

