from card import *
import copy

class Player:
	def __init__(self):
		self.hand = []
		self.bet = 0
		self.tricksWon = []
		self.score = 0

	def playCard(self, card):
		try:
			i = self.hand.index(card)
		except ValueError:
			return [False, Card()]
		return [True, self.hand.pop(i)]

	def getNullHandCopy(self):
		null_hand = []
		return null_hand

	def getCopy(self):
		copy = Player()
		copy.hand = self.hand.copy()
		copy.bet = self.bet.copy()
		copy.tricksWon = self.tricksWon.copy()
		copy.score = self.score.copy()
		return copy

	def getCopyNullHand(self):
		copy = Player()
		copy.hand = [Card()]*len(self.hand)
		copy.bet = self.bet.copy()
		copy.tricksWon = self.tricksWon.copy()
		copy.score = self.score.copy()
		return copy

	def endRound(self):
		if bet == tricksWon:
			roundScore = 20 + len(tricksWon) 10
		else:
			roundScore = -10 * abs(len(tricksWon) - bet)

		tricksWon = []		### place for tracking?

		# accumulate total score
		score = score + roundScore


