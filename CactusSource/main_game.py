class MainGame(object):
	"""
	Stores general data about the game. A MainGame instance
	contains the following attributes.
	
		name       - The name of the game.
		desc       - The game's description.
		prompt     - The global prompt to be used.
		error_msg  - A message to print if user enters invalid input.
		map_data   - The game's map data, a GameMap instance.
		lower_text - The option to lower text or not.
	"""
	def __init__(self, name: str, desc: str, prompt: str, error_msg: str, map_data, lower_text: bool):
		self.name         = name
		self.desc         = desc
		self.prompt       = prompt
		self.error_msg    = error_msg
		self.map_data     = map_data
		self.lower_text   = lower_text
		self.map_list     = self.map_data.return_map_data()
		self.map_start    = self.map_data.find_start(self.lower_text)
		self.map_position = self.map_start
		
	def play_game(self):
		"""
		Start playing the user-created game.
		"""
		while True:
			current_map_position = self.map_list[self.map_position]
			possible_choices     = current_map_position.choices
			
			current_map_position.position_enter()
			user_input = input(self.prompt)
			
			if self.lower_text:
				if user_input.lower() in possible_choices:
					self.map_position = possible_choices[user_input.lower()]
					current_map_position.position_exit()
				else:
					print(self.error_msg)
			else:
				if user_input in possible_choices:
					self.map_position = possible_choices[user_input]
					current_map_position.position_exit()
				else:
					print(self.error_msg)