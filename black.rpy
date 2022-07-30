
init python:
    
    class Card:
        
        def __init__(self, suit, val):
            self.suit = suit
            self.value = val
            
    class Deck:
        
        def __init__(self):
            self.cards = []*4
            self.build()
        
        def build(self):
            for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                for v in range(2, 14):
                    self.cards.append(Card(s, v))
        
        def show(self):
            for c in self.cards:
                c.show()
        
        def shuffle(self):
            self.cards = []*4
            self.build()
            for i in range(len(self.cards) - 1, 0, -1):
                r = renpy.random.randint(0, i)
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        
        def drawCard(self):
            drawn = self.cards.pop()
            if drawn.value == 11:drawn.value = "jack"
            if drawn.value == 12:drawn.value = "queen"
            if drawn.value == 13:drawn.value = "king"
            if drawn.value == 14:drawn.value = "ace"
            
            return drawn
        
    class Player:
        
        def __init__(self, name):
            self.name = name
            self.hand = []
        
        def draw(self, deck):
            self.hand.append(deck.drawCard())
            return self
        
        def showHand(self):
            cards = ""
            for card in self.hand:
                cards += "{} of {}".format(card.value, card.suit) + ", "
            return cards[:-2]
        
        def discard(self):
            del self.hand[:]

        def getLastCard(self):
            card = self.hand[-1]
            return "{} of {}".format(card.value, card.suit)

        def getFirstCard(self):
            drawn = 0
            if len(self.hand)>0:
                drawn = self.hand[0].value
                if drawn == "jack":drawn = 10
                if drawn == "queen":drawn = 10
                if drawn == "king":drawn = 10
                if drawn == "ace":drawn = 1
            return drawn

        def total(self):
            total = 0
            for card in self.hand:
                if card.value == "jack" or card.value == "queen" or card.value == "king":
                    total += 10
                elif card.value == "ace":
                    if total >= 11:
                        total += 1
                    else:
                        total += 11
                else:
                    total += card.value
            return total

        def cardCount(self):
            return len(self.hand)
            
            
define deck = Deck()
define player1 = Player("Your")
define dealer = Player("Dealer")
default first_bet = True

default playertotal = 0
default dealertotal = 0

default lastcard = []

label blackjack:
    scene black
    show screen stats
    show screen hands
    $ deck.shuffle()

label hand_start:
    
    call reset_hand
    $ deck.shuffle()

    $ player1.draw(deck)
    $ player1.draw(deck)
    $ dealer.draw(deck)
    $ dealer.draw(deck)
    
    $ player1_cards = player1.showHand()
    $ dealer_cards = dealer.showHand()
    
    $ first_bet = True
    $ hidden = True

    #"[player1.name] cards are [player1_cards]"
    #"[dealer.name] cards are [dealer_cards]"

label turn:
    
    menu:
        "Hit":
            $ player1.draw(deck)
            $ player1_cards = player1.showHand()
            $ first_bet = False
            "[player1_cards]"
            
            if player1.total() < 21:
                jump turn
            elif player1.total() == 21:
                jump dealer_turn
            elif player1.total() > 21:
                jump bust
            
        "Stand":
            jump dealer_turn
        
        "Double down" if first_bet:
            $ player1.draw(deck)
            $ player1_cards = player1.showHand()
            jump dealer_turn


label dealer_turn:
    
    if dealer.total() < 17:
        $ dealer.draw(deck)
        $ lastcard = dealer.getLastCard()
        "Dealer draws [lastcard]"
        jump dealer_turn
    elif dealer.total() == 21:
        jump results
    elif dealer.total() > 21:
        "Dealer Bust"
        jump win
    else:
        jump results

label bust:
    
    "Over 21, Bust"
    jump hand_start

label results:

    $ player1_cards = player1.showHand()
    $ dealer_cards = dealer.showHand()

    $ playertotal = player1.total()
    $ dealertotal = dealer.total()
    $ hidden = False

    "Your hand: [player1_cards], [playertotal]"
    "Dealer's hand: [dealer_cards], [dealertotal]"

    
    if dealer.total() == player1.total():
        jump push
    elif dealer.total() > player1.total():
        jump lose
    elif dealer.total() < player1.total():
        jump win

label push:
    
    "The hand is a push"
    jump hand_start

label lose:

    "You lose"
    jump hand_start

label win:
    
    "You win"
    jump hand_start

label reset_hand:
    
    $ player1.discard()
    $ dealer.discard()
    return

screen stats():
    
    python:
        ptotal = player1.total()
        if hidden == True:
            dtotal = dealer.total() - int(dealer.getFirstCard())
        else:
            dtotal = dealer.total()
    fixed:
        text "Your hand: [ptotal]":
            xpos 0.2
            ypos 0.05
        if hidden == True:
            text "Dealer's hand: ? + [dtotal]":
                xpos 0.8
                ypos 0.05
        else:
            text "Dealer's hand: [dtotal]":
                xpos 0.8
                ypos 0.05

screen hands():

    vpgrid:
        xalign 0.5
        yalign 0.9
        cols player1.cardCount()
        rows 1
        $ cards = player1.showHand().split(", ")
        for x in cards:
            $ y = x.replace(" ", "_") + ".png"
            image im.Scale(y,100,144)

    vpgrid:
        xalign 0.5
        yalign 0.1
        cols dealer.cardCount()
        rows 1
        $ cards = dealer.showHand().split(", ")
        for x in cards:
            if (x == cards[0]) & (hidden == True):
                image im.Scale("back.png",100,144)
            else:
                $ y = x.replace(" ", "_") + ".png"
                image im.Scale(y,100,144)

