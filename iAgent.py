
class IAgent():

	def setPlayerNumber(self, player_number):
		self.player_number = player_number

	# Simply stores new game state locally
	def updateGameState(self, sanitized_game):
		self.game = sanitized_game

	def getPlayAction(self):
		# Returns card to play
		pass
