class MapPosition(object):
	"""
	This class stores relevant data about the
	position on a map, e.g, is_accessible, or
	required_key.
	"""
	def __init__(self, desc, is_accessible=True, required_key=None, function=None):
		self.desc          = desc
		self.is_accessible = is_accessible
		self.required_key  = required_key
		self.function      = function

		
class GameMap(object):
	"""
	This class stores relevant data about the
	map, e.g, valid areas, and invalid areas.
	For example, the following map could be
	defined:
	
		my_map = GameMap([
			[ MapPosition(""), MapPosition(""), None ],
			[ None,            MapPosition(""), None ],
			[ MapPosition(""), MapPosition(""), None ]
		])
	"""
	def __init__(self, map_array):
		self.map_array = map_array