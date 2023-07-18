from main import StandardDeck

class HoldemPlayer(object): 
    def __init__(self): 
        self.cards = []
        self.user = False 



class HoldemTable(object):
    def __init__(self): 
        self.cards = []
        self.playerCount = 0
        self.big_blind = 0 
        self.small_blind = 0
        self.players = []


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





            


