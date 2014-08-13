from deck import *
from card import *
from operator import attrgetter

class Trick:
	def __init__(self, cards=[], trumpCard=WizardCard()):
		
		self.winner = -1
		self.cards = cards
		self.trumpCard = trumpCard
		self.trickCard = WizardCard()

		### Implement status reporting!

		self.trumpStatus = [
		"Last Round: No trump card",
		"Trump is a Jester: Error!",
		"Trump is a Wizard: Dealer chooses"]

		self.trickStatus = [
		"Next non-Jester determines trick suit"
		"Trick suit is Spades",
		"Trick suit is Hearts",
		"Trick suit is Clubs",
		"Trick suit is Diamonds",
		"No trick suit: Play anything!"]

		self.status = "Default Status"

		### need some sort of handler:
		# trick suit set by second player if first player plays a Jester
		# no trick suit if first player plays a Wizard
		self.trickSuit = -1
		self.trumpCards = []
		self.trickSuitCards = []
		self.otherCards = []

		if trumpCard == WizardCard():
			print("No trump card!")
		elif trumpCard == WizardCard(1, 0):
			print("Trump is a Jester")
		elif trumpCard == WizardCard(15, 5):
			print("Trump is a Wizard")
		else:
			print("Trump card: %s", trumpCard)

	def __repr__(self):
		trick_str = ""
		for card in self.cards:
			trick_str += "%s" % card
		return trick_str

	def getTrickCard (self):
		### assume all cards are already in the trick list
		if self.cards[0] == WizardCard(15,5):
			# no suit - null suit already set in constructor

			### status: no trick suit!
			return WizardCard()
		elif self.cards[0] == WizardCard(1,0):
			# cycle through to find first non-Jester card
			for c in self.cards:
				if c != WizardCard(1,0): 
					return c
			### status: no trick suit yet!
			return WizardCard()
		else:

			### status: trick suit = self.cards[0].suit
			return self.cards[0]
		
	def getHighestCard(self, cardArray=[WizardCard()]):
		return sorted(cardArray, key=attrgetter('rank'), reverse=True)[0]

	def determineWinner (self):

		### Do we need to check length of cards[] > 0?  should have check prior to this code
		self.trickCard = self.getTrickCard()

		# If all Jesters are played, first player wins the trick
		if self.cards == [WizardCard(1,0)]*len(self.cards):
			return 0

		# Otherwise look through trick and pick out the winner
		for idx, c in enumerate(self.cards):
			# look for the first wizard, immediately return if found
			if c.suit == 5:
				self.winner = idx
				break
			# create array of trump suit cards
			elif c.suit == self.trumpCard.suit:
				self.trumpCards.append(c)
			elif c.suit == self.trickCard.suit:
				self.trickSuitCards.append(c)

		if self.winner > -1:
			return self.winner		#wizard found
		elif len(self.trumpCards) > 0:
			# sort trump cards and return highest
			self.winner = self.cards.index(self.getHighestCard(self.trumpCards))
		else:
			self.winner = self.cards.index(self.getHighestCard(self.trickSuitCards))

		return self.winner




