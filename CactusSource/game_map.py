class GameMap(object):
    """
    Stores general data about a game map. A GameMap
    instance contains the following data.
    
        data - A list of MapPosition instances representing a game map.
    """
    def __init__(self, data: list):
        self.data = data
        
    def find_start(self, should_lower_text: bool):
        """
        This iterates over self.data and finds the MapPosition
        instance with the name of start, and returns it's index.
        """
        for index, map_position in enumerate(self.data):
            if should_lower_text:
                if map_position.name.lower() == "start":
                    return index
            else:
                if self.map_position.name == "start":
                    return index
