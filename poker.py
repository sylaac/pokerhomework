import random
suits = ["♠", "♥", "♦", "♣"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_twopair(self):
        paircounter = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    paircounter += 1
        if paircounter == 2:
            return True
        if paircounter > 2:
            return paircounter
        else:
            return False

    def is_threeofakind(self):
        for i in range(5):
            triplecounter = 1
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    triplecounter += 1
                    if triplecounter == 3:
                        return True
        return False

    def is_straight(self):
        order = []
        if  not self.is_pair():
            for i in range(5):
                order.append(self.cards[i].get_rank())
            for rank in order :
                rank = int(rank)
            order.sort()
            if 2 in order and 13 not in order :
                while 14 in order :
                    order[4]= 1
                    order.sort()
            if int(order[0])-int(order[4]) == -4:
                if 13 and 14 in order:
                    return "royal possible"
                return True
        return False

    def is_flush(self):
        color = self.cards[0].get_suit()
        for i in range(5):
            if self.cards[i].get_suit() != color :
                return False
        else :
            return  True

    def is_fullhouse(self):
        if self.is_twopair() != 3 and self.is_threeofakind():
            return True
        else:
            return False

    def is_fourofakind(self):
        for i in range(5):
            quadruple = 1
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    quadruple += 1
                    if quadruple == 4:
                        return True
        return False

    def is_straightflush(self):
        if self.is_straight() and self.is_flush():
            return True
        else:
            return False
    def is_royalstraightflush(self):
        if self.is_straightflush() and self.is_straight() == "royal possible":
            return "Lucky"






tries = 100000
royal_straight_flush = 0
straight_flush = 0
four_of_a_kind = 0
fullhouse = 0
flush = 0
straight = 0
three_of_a_kind = 0
two_pairs = 0
for i in range(tries):
    new_deck = Deck()
    new_deck.shuffle()
    hand = Hand(new_deck)
    if hand.is_royalstraightflush():
        print(hand)
        royal_straight_flush += 1
    elif hand.is_straightflush():
        straight_flush += 1
    elif hand.is_fourofakind():
        four_of_a_kind += 1
    elif hand.is_fullhouse():
        fullhouse += 1
    elif hand.is_flush():
        flush += 1
    elif hand.is_straight():
        straight += 1
    elif hand.is_threeofakind():
        three_of_a_kind += 1
    elif hand.is_twopair():
        two_pairs += 1

print("royal_straight_flush",royal_straight_flush/tries*100,"%")
print("straight_flush",straight_flush/tries*100,"%")
print("four_of_a_kind",four_of_a_kind/tries*100,"%")
print("fullhouse",fullhouse/tries*100,"%")
print("flush",flush/tries*100,"%")
print("straight:",straight/tries*100,"%")
print("three of a kind:",three_of_a_kind/tries*100,"%")
print("two pairs",two_pairs/tries*100,"%")