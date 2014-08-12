import random
import copy
from card import *

# Inherits from CardCollection class, adds shuffle capability
class WizardDeck:
	def __init__(self):
		self.cards = []

		# Add normal cards to deck for a deck of 52
		for suit in range(1, 5):
			for rank in range(2,15):
				self.cards.append(WizardCard(rank, suit))

		# Add wildcards
		for idx in range(0, 4):
			self.cards.append(WizardCard(1, 0))
			self.cards.append(WizardCard(15, 0))
				
	def shuffle(self):
		random.shuffle(self.cards)
		
	def cardsLeft(self):
		return len(self.cards)
		
	def getTopCard(self):
		return self.cards.pop(0)

	def peekTopCard(self):
		return copy.copy(self.cards[0])
		
	def __repr__(self):
		string = ""
		for idx in range(0,52):
			string += "%d: %s\n" %(idx + 1, self.cards[idx])
		return string


class NullDeck():
	def __init__(self, cards_left=0):
		self.cards = []
		self.cards_left= cards_left;

	def cardsLeft(self):
		return self.cards_left
	
	def __repr__(self):
		string = ""
		for idx in range(0,52):
			string += "%d: %s\n" %(idx + 1, self.cards[idx])
		return string
