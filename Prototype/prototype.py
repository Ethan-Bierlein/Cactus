class MapPosition(object):
	"""
	Describes data about a position on in the world
	map. Contains the following data attributes.
	
		name     - The name of the choice.
		choices  - A dictionary of possible choices.
		function - An (optional) function to be run.
	"""
	def __init__(self, name, choices, function=None):
		self.name     = name
		self.choices  = choices
		self.function = function
		
	def run_function(self):
		"""
		Run the attached function when the choice is chosen
		by the user.
		"""
		if self.function is not None:
			self.function()

		
class GameMap(object):
	"""
	Describes data about a world map. Contains the
	following data attributes.
	
		map_data - A list containing MapPosition's
	"""
	def __init__(self, map_data):
		self.map_data = map_data
		
	def find_start(self):
		"""
		This iterates over the self.map_data list and finds
		the starting choice.
		"""
		for index, choice in enumerate(self.map_data):
			if choice.name.lower() == "start":
				return index
			else:
				continue
		
	def return_map(self):
		"""
		Returns the map_data as a list.
		"""
		return self.map_data
		
	
class MainGame(object):
	"""
	Describes data about the game itself. Contains
	the following data attributes.
	
		game_map    - A GameMap instance containing map data.
		player_data - A Player instance containing player data.
	"""
	def __init__(self, game_map, player_data):
		self.game_map    = game_map
		self.player_data = player_data
		self.map_data    = game_map.return_map()
		self.start_index = game_map.find_start()
		
	def play_game(self):
		"""
		Start playing the game. This function will find the
		MapPosition element that has the name "start".
		"""
		pass