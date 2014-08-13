import copy
from player import *
from deck import *
from meld import *

class Game:
	def __init__(self, numPlayers):

		# Calculate number of tricks
		self.totalRounds = 60 / numPlayers;
		self.currentRound = 0		#0 for dealer determination round

		self.rounds = []
		self.tricks = []
		
		# Define lists for players and populate it
		self.players = []
		for num in range(numPlayers):
			self.players.append(Player())

	def __repr__(self):
		draw_pile_str = "Draw Pile: %d Cards Left\n\n" % (self.draw_pile.cardsLeft())

		discard_pile_str = "Discard Pile:\n"
		for idx in range(len(self.discard_pile)):
			discard_pile_str += '%d: %s\n' %((len(self.discard_pile) - idx), self.discard_pile[idx].__repr__())

		player_str = ""
		meld_type_dict = {1: "Run", 2: "Str"}
		for p in range(len(self.players)):
			player_str += "\nPlayer %d\n" % (p+1)
			player_str += "========================================\n\n"
			player_str += "Board:\n"
			for meld in self.players[p].board:
				player_str += "%s: %s\n" %(meld_type_dict.get(meld.meld_type), meld)
			# Check for null card as first card, if its null, print the number of cards out
			# Otherwise print the players hand via index
			if(self.players[p].hand[0] == Card()):
				player_str += "\nHand: %d Cards\n\n" % len(self.players[p].hand)
			else:
				player_str += "\nHand:\n"
				for idx in range(len(self.players[p].hand)):
					player_str += ("%d: %s\n" %(idx, self.players[p].hand[idx]))

		return draw_pile_str + discard_pile_str + player_str

	def numPlayers(self):
		return len(self.players)

	def getSanitizedCopy(self, agent_num):
		copy = Game(len(self.players))
		copy.players = []
		for i in range(len(self.players)):
			if i != agent_num:
				copy.players.append(self.players[i].getCopyNullHand())
			else:
				copy.players.append(self.players[i].getCopy())
		copy.discard_pile = self.discard_pile.copy()
		copy.draw_pile = NullDeck(self.draw_pile.cardsLeft())
		return copy
