import unittest

from deck import *

class WizardDeckTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor(self):
		test_deck = []
		for suit in range(1, 5):
			for rank in range (2, 15):
				test_deck.append(WizardCard(rank, suit))
		for idx in range(0, 4):
			test_deck.append(WizardCard(1, 0))
			test_deck.append(WizardCard(15, 0))

		d = WizardDeck()
		self.assertEqual(d.cardsLeft(), 60)
		self.assertEqual(d.cards, test_deck)
		
	def test_shuffle(self):
		d = WizardDeck()
		d.shuffle()
		self.assertEqual(d.cardsLeft(), 60)
		
	def test_get_top_card(self):
		d = WizardDeck()
		d.shuffle()
		top_card = d.cards[0]
		self.assertEqual(d.getTopCard(), top_card)
		self.assertEqual(d.cardsLeft(), 59)

if __name__ == '__main__':
	unittest.main()

