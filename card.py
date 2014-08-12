# null card is rank = 0, suit = 0
# Jester is rank = 1
# Wizard is rank = 15

class WizardCard:

	# Define face cards
	face_cards = {-1: 'NUL', 1: 'JES', 10: '10 ', 11:'JAK', 12:'QEN', 13:'KNG', 14:'ACE', 15:'WIZ'}
	# Define suits, 0 is a wildcard suit (represents all suits)
	suits = {-1: 'N', 0: 'WILD', 1: 'S', 2: 'H', 3: 'C', 4: 'D'}

	def __init__(self, rank=-1, suit=-1):
		self.rank = rank
		if rank == 1 or rank == 15:
			self.suit = 0
		else:
			self.suit = suit
		
	def __repr__(self, debug=False):
		# Return face card rank if in dict, otherwise return string of the rank (2-9)
		readable_rank = self.face_cards.get(self.rank, str(self.rank) + '  ')
		#readable_alt_rank = self.face_cards.get(self.alt_rank, str(self.alt_rank) + ' ')
		readable_suit = self.suits.get(self.suit)

		return "<%s %s>" % (readable_rank, readable_suit)
		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.suit == other.suit and self.rank == other.rank
		else:
			return False
