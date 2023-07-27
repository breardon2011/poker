import random
from holdem import * 
# The Card / Deck / poker scorer / video poker routing from:  https://www.youtube.com/watch?v=z84oyxItl18



class Card( object ):
  def __init__(self, name, value, suit, symbol):
    self.value = value
    self.suit = suit
    self.name = name
    self.symbol = symbol
    self.showing = False

  def __repr__(self):
    if self.showing:
      return self.symbol
    else:
      return "Card"

class Deck(object):
  def shuffle(self, times=1 ):
    random.shuffle(self.cards)
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)

class StandardDeck(Deck):
  def __init__(self):
    self.cards = []
    suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
    values = {"Two":2,
              "Three":3,
              "Four":4,
              "Five":5,
              "Six":6,
              "Seven":7,
              "Eight":8,
              "Nine":9,
              "Ten":10,
              "Jack":11,
              "Queen":12,
              "King":13,
              "Ace":14 }

    for name in values:
      for suit in suits:
        symbolIcon = suits[suit]
        if values[name] < 11:
          symbol = str(values[name])+symbolIcon
        else:
          symbol = name[0]+symbolIcon
        self.cards.append( Card(name, values[name], suit, symbol) )

  def __repr__(self):
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

class Player(object):
  def __init__(self):
    self.cards = []

  def cardCount(self):
    return len(self.cards)

  def addCard(self, card):
    self.cards.append(card)


class PokerScorer(object):
  def __init__(self, cards):
    # Number of cards
    if not len(cards) == 5:
      return "Error: Wrong number of cards"

    self.cards = cards

  def flush(self):
    suits = [card.suit for card in self.cards]
    if len( set(suits) ) == 1:
      return True
    return False

  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()

    if not len( set(values)) == 5:
      return False 

    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5

    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False

    return values[4]

  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card

    return highCard

  def highestCount(self):
    count = 0
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)

    return count

  def pairs(self):
    pairs = []
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)

    return pairs
        
  def fourKind(self):
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 4:
        return True

  def fullHouse(self):
    two = False
    three = False
    
    values = [card.value for card in self.cards]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True

    if two and three:
      return True

    return False

def interpreterVideoPoker():
  player = Player()

  # Intial Amount
  points = 100

  # Cost per hand
  handCost = 5

  end = False
  while not end:
    print( "You have {0} points".format(points) )
    print()

    points-=5

    ## Hand Loop
    deck = StandardDeck()
    deck.shuffle()

    # Deal Out
    for i in range(5):
      player.addCard(deck.deal())

    # Make them visible
    for card in player.cards:
      card.showing = True
    print(player.cards)

    validInput = False
    while not validInput:
      print("Which cards do you want to discard? ( ie. 1, 2, 3 )")
      print("*Just hit return to hold all, type exit to quit")
      inputStr = input()

      if inputStr == "exit":
        end=True
        break

      try:
        inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

        for inp in inputList:
          if inp > 6:
            continue 
          if inp < 1:
            continue 

        for inp in inputList:
          player.cards[inp-1] = deck.deal()
          player.cards[inp-1].showing = True

        validInput = True
      except:
        print("Input Error: use commas to separated the cards you want to hold")

    print(player.cards)
    #Score
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # Royal flush
    if straight and flush and straight == 14:
      print("Royal Flush!!!")
      print("+2000")
      points += 2000

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      print("+250")
      points += 250

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      print("+125")
      points += 125

    # Full House
    elif score.fullHouse():
      print("Full House!")
      print("+40")
      points += 40

    # Flush
    elif flush:
      print("Flush!")
      print("+25")
      points += 25

    # Straight
    elif straight:
      print("Straight!")
      print("+20")
      points += 20

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      print("+15")
      points += 15

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("+10")
      points += 10

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("+5")
      points += 5

    player.cards=[]

    print()
    print()
    print()


def holdem_game():
    print("Hold em!")
    table = HoldemTable()
    doneWithPlayerCount = False
    while not doneWithPlayerCount: 
        print("How many AI players should there be?")
        print("type a number between 1-7. Type exit to quit")
        inputStr = input()
        if inputStr == "exit":
            break
        
        try:
            numberOfPlayers = int(inputStr)
            if numberOfPlayers > 7: 
                print("\n\n")
                print("The max number of seats is 8, counting you.")
                print("\n\n")
                continue
            if numberOfPlayers < 1: 
                print("\n\n")
                print("Poker needs at least 2 players, counting you")
                print("\n\n")
                continue 
            else: 
                table.playerCount = numberOfPlayers
                doneWithPlayerCount = True

        except Exception as e:
            print("There is an error: " + e) 
    print("The player count = " + str(1 + table.playerCount))
    
    table.createPlayers()
    
    doneWithBlinds = False 
    while not doneWithBlinds: 
        print("What should the big blind be?")
        print("It should be an even number, the small blind will be half")
        print("Enter an even number between 2-1000")
        inputStr = input()
        try: 
            blinds = int(inputStr)
            if blinds > 1000: 
                print("\n\n")
                print("If you want higher stakes you need to go to Moncao buddy!")
                print("\n\n")
                continue
            if blinds < 2: 
                print("\n\n")
                print("The blinds need to be higher than 2, no 50 cent chips in this casino!")
                print("\n\n")
                continue 
            if blinds%2 != 0: 
                print("\n\n")
                print("Need to be an even number!")
                print("\n\n")               
            
            else: 
                table.big_blind = blinds
                table.small_blind = int(blinds/2)
                doneWithBlinds = True
        except Exception as e: 
            print("There is an error: " + e)
    
    print("The blinds for this table are " + str(table.small_blind)+ "/" + str(table.big_blind))

    deck = StandardDeck() 
    deck.shuffle() 

    #Game loop 

    # for each player deal 2 cars
    for player in table.players: 
      player.addCard(deck.deal()) #find way to do deck.deal(2) 
      player.addCard(deck.deal())
    # display player cards
    for card in table.user.cards: 
      card.showing = True 

    print(table.user.cards) 

    #other players bet if first 

    #bet calculation
    # if bet to them is > big blind 
    # show bet to them 
    # are they big or small blind

    # what does it cost to play



if __name__ == "__main__":
  holdem_game()