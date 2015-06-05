class GameMap(object):
	"""
	Stores general data about a game map. A GameMap
	instance contains the following data.
	
		map_data - A list of MapPosition instances representing a game map.
	"""
	def __init__(self, map_data: list):
		self.map_data = map_data
		
	def find_start(self, lower_text: bool):
		"""
		This iterates over self.map_data and finds the MapPosition
		instance with the name of start, and returns it's index.
		"""
		for index, map_position in enumerate(self.map_data):
			if lower_text:
				if map_position.name.lower() == "start":
					return index
			else:
				if self.map_position.name == "start":
					return index
					
	def return_map_data(self):
		"""
		Returns self.map_data as a list.
		"""
		return self.map_data