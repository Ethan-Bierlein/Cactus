class MapPosition(object):
	"""
	Stores general data about a position on the
	map. A MapPosition instance contains the 
	following data.
	
		name       - The name of the MapPosition.
		desc_enter - A description of the MapPosition displayed when the player enters.
		desc_exit  - A description of the MapPosition displayed when the player exits.
		choices    - A dictionary referencing other possible choices, e.g, indexes in the map.
		function   - An optional function to be run before desc_enter is displayed.
	"""
	def __init__(self, name: str, desc_enter: str, desc_exit: str, choices: dict, function=None):
		self.name       = name
		self.desc_enter = desc_enter
		self.desc_exit  = desc_exit
		self.choices    = choices
		self.function   = function
		
	def _position_enter(self):
		"""
		Output the various data associated with a MapPosition when 
		the player enters the MapPosition. 
		"""
		if self.function is not None:
			self.function()

		if self.choices != {}:
			print(
				"{0}: {1} Choices: {2}".format(
					self.name      ,
					self.desc_enter,
					', '.join([key for key value in self.choices.items()])
				)
			)
		else:
			print(
				"{0}: {1} Choices: {2}".format(
					self.name      ,
					self.desc_enter,
				)
			)
			
	def _position_exit(self):
		"""
		Output the various data associated with a MapPosition when
		the player exits the MapPosition.
		"""
		print self.desc_exit