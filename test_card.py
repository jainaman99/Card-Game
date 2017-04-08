from cards import Card,Deck
from game import Game,Player
import unittest

class testCardMethods(unittest.TestCase):
    def test_card_init(self):
        c = Card("spade",4)
        self.assertEquals(c.suit,"spade", "card suite is set properly")
        self.assertEquals(c.value,4, "card value is set properly ")


class testDeckMethods(unittest.TestCase):
    def test_deck_init(self):
        deck = Deck()
        self.assertEquals(len(deck.cards),52,"deck size is proper")
        self.assertIsInstance(deck.cards[0],Card,"deck card is instance of Card")
    
    def test_deck_draw_random_card(self):
        deck = Deck()
        self.assertEquals(len(deck.cards),52,"deck size is proper")
        self.assertIsInstance(deck.cards[0],Card,"deck card is instance of Card")
        dc = deck.draw_random_card()
        self.assertIsInstance(dc,Card,"drawn card data type is correct")
        self.assertTrue(dc.value >=1 and dc.value <=52, "drawn card value is correct")
        self.assertEquals(len(deck.cards),51,"deck length is decreased by one properly")

    def test_shuffle_cards(self):
        print "going to shuffle cards"
        deck = Deck()
        deck.shuffle_cards()