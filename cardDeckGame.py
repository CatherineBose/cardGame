from random import shuffle

class Card(object):
    def __init__(self,suits,cardvalue):
        self.suits = suits
        self.cardvalue = cardvalue

class Deck(object):
    def __init__(self,name):
        self.numcards = []
        self.totalCardsAvailable = len(self.numcards)
        self.deckName = name
    def shufflecards(self):
        shuffle(self.numcards)
    def createDeck(self):
        suits=["spades","diamonds","hearts","clubs"]
        cardvalue=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for i in range(0,4):
            for x in range(0,13):
                cardsInDeck = Card(suits[i],cardvalue[x])
                # all cards are stored in num array
                self.numcards.append(cardsInDeck)
                # print "card1 Suits {} card1 value {}".format( card1.suits,card1.cardvalue)
        return self
    def deal(self,user):
        print "Hi player",user.name
        print "Total cards available in ",self.deckName,":",self.totalCardsAvailable
        print "########We are Dealing now lets shuffle!!!##########"
        self.shufflecards()
        self.totalCardsAvailable = len(self.numcards) 
        
        print "Each player gets 5 cards by default"
        if(user.age<21):
            print "We don't deal with minors ####Go back to kids zone###"
        elif(self.totalCardsAvailable>=5 and user.totalCardsInHand<=0 and user.age>22):  
            # for i in range (totalCardsAvailable,totalCardsAvailable-6,-1):
            for i in range (1,6):
                # user.hand.append(self.numcards[i])
                user.hand.append(self.numcards.pop())
                user.totalCardsInHand += 1
                # print "Card added in hand is",user.hand[(len(user.hand))-1].suits,":",user.hand[(len(user.hand))-1].cardvalue
            return user.hand
class Player(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hand = []
        self.totalCardsInHand = 0
        # decklist is obj of deck
    def drawfromdeck(self,deckList):
        print "########Drawing a card from deck!!#######"
        for i in range (1, 2):
            self.hand.append(deckList.pop())
            self.totalCardsInHand += 1
            deckList.totalCardsAvailable -= 1
            print "One card drawn from deck, total avilable cards:", deckList.totalCardsAvailable
            print "Total no of cards in hand is:", self.totalCardsInHand
            print "You need to return a card back in lui of a card drawn"
        return self
        #for x in range (1,totalCardsInHand+1):
        #     print "Cards in my hand"
        #     print "cardvalue:", self.hand[x].cardvalue
    def showcardsinhand(self):
        print "######Show Cards player {}#########".format(self.name)
        for x in range (0,5):
            print "Suit: {} Card Value: {}".format(self.hand[x].suits,self.hand[x].cardvalue)
            # print "cardvalue:", self.hand[x].cardvalue
            # print "Suit:", self.hand[x].suits
        return self

# instance of deck
deck1 = Deck("deck1")
# create a player
player1 = Player("Phil","23")
# create a deck and deal
deck1.createDeck().deal(player1)
# Players shows the cards
player1.showcardsinhand()
# Player draws from deck
player1.drawfromdeck(deck1.numcards)
