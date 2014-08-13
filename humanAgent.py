from iAgent import *
from meld import *
from operator import attrgetter
import os

class HumanAgent(IAgent):
	
	# do I need this?
	def __init__(self):
		self.players = []
		self.discard_pile = []
		
	def getPlayAction(self):

		os.system('cls' if os.name=='nt' else 'clear')		

		print ("Current Game State:")
		self.game.players[self.player_number].hand = sorted(self.game.players[self.player_number].hand, key=attrgetter( 'rank', 'suit'))
		print (self.game)
		print ("")
		print ("Actions:")
		print ("N: Play Card at index N, (0 based)")
		
		discard_action = -2 # This will be set by the user 
		while(True):
			discard_action_str = input("What would you like to do? ")
			
			if (len(discard_action_str) == 0):
				print("Invalid choice!\n")
				continue

			try:
				discard_action = int(discard_action_str)
			except:
				print("Must input an integer!\n")
				continue

			if ((discard_action >= -1) and (discard_action < len(self.game.players[self.player_number].hand))):
				break
			print ("Invalid choice entered, try again.")
		
		c = self.game.players[self.player_number].hand[discard_action]
		print ("Playing %s." % c)
		return c
