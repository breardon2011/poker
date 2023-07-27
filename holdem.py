PLAYER_NAMES = ["Phil", "Dennis", "Bill","Jason", "Matt", "Ron", "Eddie", "Robert", "Rita", "Jean", "Paula", "Kevin", "Mike"]


class HoldemPlayer(object): 
    def __init__(self): 
        self.cards = []
        self.user = False
        self.name = ""
    def addCard(self, card):
        self.cards.append(card)



class HoldemTable(object):
    def __init__(self): 
        self.cards = [] # flop etc
        self.playerCount = 0 #AI count 
        self.big_blind = 0 #position 
        self.small_blind = 0 #position 
        self.players = [] #player objects
        self.current_pot = 0 
        self.user = None 
    
    def createPlayers(self): 
        for player in range(self.playerCount):
            new_player = HoldemPlayer()
            new_player.name = PLAYER_NAMES[player]
            self.players.append(new_player)
        #create user player
        user = HoldemPlayer()
        user.name = 'user' 
        user.user = True
        self.players.append(user)
        self.user = user 
            







            


