from random import shuffle

class Card(object):
    def __init__(self,suits,cardvalue):
        self.suits = suits
        self.cardvalue = cardvalue
    
        
        
class Deck(object):
    def __init__(self):
        self.numcards = []
    def shufflecards(self):
        shuffle(self.numcards)
    def create_Deck(self):
        suits=["spades","diamonds","hearts","clubs"]
        cardvalue=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for i in range(0,4):
            for x in range(0,13):
                card1 = Card(suits[i],cardvalue[x])
                # all cards are stored in num array
                self.numcards.append(card1)
                # print "card1 Suits {} card1 value {}".format( card1.suits,card1.cardvalue)
        return self
    def deal(self,user):
        print "We are Dealing now!!!"
        print "Each player gets 5 cards by default"
        totalCardsAvailable = len(self.numcards) 
        print "Total cards available:"
        # print totalCardsAvailable
        # for i in range (totalCardsAvailable,totalCardsAvailable-6,-1):
        for i in range (0,6):
            # print "numcards:", self.numcards
            # print "self.numcards[i]: ", self.numcards[i].cardvalue, self.numcards[i].suits
            user.hand.append(self.numcards[i])
        # for x in range (1,6):
        #     print "our hand consists of:"
        #     print "value", user.hand[x].cardvalue, "suits", user.hand[x].suits
            return user.hand
class Player(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hand = []
        # decklist is obj of deck
    def drawfromdeck(self,deckList):
        for i in range (1, 6):
            self.hand.append(deckList.pop())
        for x in range (1,6):
            print "Cards in my hand"
            print "cardvalue:", self.hand[x].cardvalue
    def showcardsinhand(self):
        for x in range (0,5):
            print "Show Cards"
            print "cardvalue:", self.hand[x].cardvalue
            print "Suit:", self.hand[x].suits
            return self.hand

# instance of deck
deck1 = Deck()
# create the deck function
deck1.create_Deck()
# create a player
player1 = Player("Phil","23")

# Shuffle cards
deck1.shufflecards()
# deck will deal now
deck1.deal(player1)
# Player draws from deck
player1.drawfromdeck(deck1.numcards)
# Players shows the cards
player1.showcardsinhand()