class CactusMap(object):
    """
    Stores general data about a game map. A CactusMap
    instance contains the following data:
    
        class_data["data"] - A list of CactusPosition instances representing a game map.
    """
    def __init__(self, class_data: dict):
        self.class_data         = class_data
        self.game               = None
        self._conditional_lower = None
        
    def set_game(self, game):
        """
        Sets the game instance this object belongs to.
        """
        self.game = game
        self._conditional_lower = self.game._conditional_lower
            
    def find_start(self):
        """
        This calls self.find_by_name() to find the position
        of the CactusPosition instance with the name "start".
        """
        return self.find_by_name("start")
        
    def find_by_name(self, name: str):
        """
        This iterates over self.class_data["data"] and finds the CactusPosition
        instance with the name specifies, and returns it's index.
        """
        for index, cactus_position in enumerate(self.class_data["data"]):
            if self._conditional_lower(cactus_position.class_data["name"]) == self._conditional_lower(name):
                return index
        return -1  # Element not found
