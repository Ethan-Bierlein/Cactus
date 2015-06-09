class Flowchart(object):
    """
    Stores general data about the game flowchart. A Flowchart
    instance contains the following data:
    
        class_data["data"] - A list of Position instances representing a flowchart.
    """
    def __init__(self, class_data: dict):
        self.class_data         = class_data
        self.game               = None
        self._conditional_lower = None
        self._check_class_data()
            
    def _check_class_data(self):
        """
        Iterate over the contained class data in self.class_data
        and make sure that it's valid.
        """
        class_data_keys = [["data", list]]
        for item in class_data_keys:
            if item[0] in self.class_data:
                if type(self.class_data[item[0]]) == item[1]:
                    continue
                else:
                    raise TypeError("Type of item {0} is invalid.".format(item[0]))
            else:
                raise KeyError("Could not find key {0} in class data.".format(item[0]))
        
    def set_game(self, game):
        """
        Sets the game instance this object belongs to.
        """
        self.game = game
        self._conditional_lower = self.game._conditional_lower
            
    def find_start(self):
        """
        This calls self.find_by_name() to find the position
        of the Position instance with the name "start".
        """
        return self.find_by_name("start")
        
    def find_by_name(self, name: str):
        """
        This iterates over self.class_data["data"] and finds the Position
        instance with the name specifies, and returns it's index.
        """
        for index, position in enumerate(self.class_data["data"]):
            if self._conditional_lower(position.class_data["name"]) == self._conditional_lower(name):
                return index
        return -1  # Element not found
