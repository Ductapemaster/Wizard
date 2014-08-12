import unittest

from card import *

class CardTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_constructor_works_as_expected(self):
		rank = 3
		suit = 2
		c = WizardCard(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

	def test_constructor_with_face_card(self):
		rank = 12
		suit = 3
		c = WizardCard(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

	def test_constructor_with_ace(self):
		rank = 14
		suit = 2
		c = WizardCard(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

	def test_constructor_with_Jester(self):
		rank = 1
		suit = 0
		c = WizardCard(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

	def test_constructor_with_wizard(self):
		rank = 15
		suit = 0
		c = WizardCard(rank, suit)
		self.assertEqual(c.rank, rank)
		self.assertEqual(c.suit, suit)

	def test_constructor_with_null_card(self):
		c = WizardCard()
		self.assertEqual(c.rank, -1)
		self.assertEqual(c.suit, -1)

if __name__ == '__main__':
	unittest.main()

