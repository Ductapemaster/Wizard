import unittest

from card import *	
from meld import *
from trick import *

class TrickTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_with_empty_trick(self):
		t = Trick()
		self.assertEqual(t.winner, -1)
		self.assertEqual(t.trickSuit, -1)
		self.assertEqual(t.trumpCards, [])
		self.assertEqual(t.trickSuitCards, [])

	def test_get_highest_card_method_standard_cards (self):
		test_cards = [WizardCard(4,1), WizardCard(11,3)]
		t = Trick(test_cards)
		self.assertEqual(t.getTrickCard(), test_cards[0])
		self.assertEqual(t.getHighestCard(t.cards), test_cards[1])

	def test_trick_with_normal_cards (self):
		test_cards = [WizardCard(4,1), WizardCard(11,3), WizardCard(8,1)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 2)
		self.assertEqual(t.trickCard, test_cards[0])

	def test_trick_with_one_wizard (self):
		test_cards = [WizardCard(4,1), WizardCard(15,5), WizardCard(8,1)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 1)
		self.assertEqual(t.trickCard, test_cards[0])

	def test_trick_with_two_wizards (self):
		test_cards = [WizardCard(4,1), WizardCard(15,5), WizardCard(15,5)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 1)
		self.assertEqual(t.trickCard, test_cards[0])

	def test_trick_with_jester (self):
		test_cards = [WizardCard(4,1), WizardCard(1,0), WizardCard(7,2)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 0)
		self.assertEqual(t.trickCard, test_cards[0])

	def test_trick_with_wizard_and_Jester (self):
		test_cards = [WizardCard(4,1), WizardCard(1,0), WizardCard(15,5)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 2)
		self.assertEqual(t.trickCard, test_cards[0])

	def test_trick_with_all_wizards (self):
		test_cards = [WizardCard(15,5), WizardCard(15,5), WizardCard(15,5)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 0)
		self.assertEqual(t.trickCard, WizardCard())

	def test_trick_with_all_Jesters (self):
		test_cards = [WizardCard(1,0), WizardCard(1,0), WizardCard(1,0)]
		t = Trick(test_cards)
		self.assertEqual(t.determineWinner(), 0)
		self.assertEqual(t.trickCard, WizardCard())



if __name__ == '__main__':
	unittest.main()  
