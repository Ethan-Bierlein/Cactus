class GameMap(object):
    """
    Stores general data about a game map. A GameMap
    instance contains the following data.
    
        data - A list of MapPosition instances representing a game map.
    """
    def __init__(self, data: list):
        self.data = data
        self.game = None
        
    def set_game(self, game):
        """
        Sets the game instance this object belongs to.
        """
        self.game = game
        
    def find_start(self):
        """
        This calls self.find_by_name() to find the position
        of the MapPosition instance with the name "start".
        """
        return self.find_by_name("start")
        
    def find_by_name(self, name: str):
        """
        This iterates over self.data and finds the MapPosition
        instance with the name specifies, and returns it's index.
        """
        for index, map_position in enumerate(self.data):
            if self.game._conditional_lower(map_position.name) == self.game._conditional_lower(name):
                return index
        return -1  # Element not found