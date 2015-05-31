class MapPosition(object):
	"""
	Describes data about a position on in the world
	map. Contains the following data attributes.
	
		name     - The name of the choice.
		desc     - A description of the choice.
		choices  - A dictionary of possible choices.
		function - An (optional) function to be run.
	"""
	def __init__(self, name, desc, choices, function=None):
		self.name     = name
		self.desc     = desc
		self.choices  = choices
		self.function = function
		
	def print_choice(self):
		"""
		Outputs certain data about the choice, e.g, description,
		it's name, possible choices, etc.
		"""
		if self.choices != {}:
			print "{0}: {1}. Choices: {2}".format(
				self.name,
				self.desc,
				', '.join([key for key, value in self.choices.iteritems()])
			)
		else:
			print "{0}: {1}.".format(
				self.name,
				self.desc
			)
		
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
	
		name        - The name of the game.
		desc        - The intro text to be printed.
		prompt      - The prompt to use during gameplay.
		game_map    - A GameMap instance containing map data.
	"""
	def __init__(self, name, desc, prompt, game_map):
		self.name         = name
		self.desc         = desc
		self.prompt       = prompt
		self.game_map     = game_map
		self.map_data     = game_map.return_map()
		self.start_index  = game_map.find_start()
		self.map_position = self.start_index
		
	def play_game(self):
		"""
		Start playing the game. This function will find the
		MapPosition element that has the name "start". Do note,
		user input is lowered, but a check is also done on non-
		lowered input.
		"""
		print self.name
		print self.desc
		
		while True:
			current_position = self.map_data[self.map_position]
			possible_choices = current_position.choices
			
			current_position.print_choice()
			current_position.run_function()
			
			user_input = raw_input(self.prompt)
			
			if user_input.lower() in possible_choices:
				self.map_position = possible_choices[user_input.lower()]
			elif user_input in possible_choices:
				self.map_position = possible_choices[user_input]