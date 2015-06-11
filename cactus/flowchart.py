from .errors import _cactus_class_method_exception_handle

class Flowchart(object):
    """
    Stores general data about the game flowchart. A Flowchart
    instance contains the following data:
    
        class_data["data"] - A list of Position instances representing a flowchart.
    """
    def __init__(self, class_data: dict):
        self.class_data         = class_data
        self._game               = None
        self._conditional_lower = None
        self._check_class_data()
    
    @_cactus_class_method_exception_handle
    def _check_class_data(self):
        """
        Iterate over the contained class data in self.class_data
        and make sure that it's valid.
        """
        CLASS_DATA_KEYS_TYPES = [["data", list]]
        CLASS_DATA_KEYS       = ["data"]
        for item in CLASS_DATA_KEYS_TYPES:
            if item[0] in self.class_data:
                if type(self.class_data[item[0]]) == item[1]:
                    continue
                else:
                    raise TypeError("Type of item '{0}' is invalid.".format(item[0]))
            else:
                raise KeyError("Could not find key '{0}' in class data.".format(item[0]))
                
        for key, value in self.class_data.items():
            if key in CLASS_DATA_KEYS:
                continue
            else:
                raise KeyError("Key '{0}' is invalid.".format(key))
    
    @_cactus_class_method_exception_handle
    def _set_game(self, game):
        """
        Sets the game instance this object belongs to.
        """
        self._game = game
        self._conditional_lower = self._game.conditional_lower
    
    @_cactus_class_method_exception_handle
    def find_start(self):
        """
        This calls self.find_by_name() to find the position
        of the Position instance with the name "start".
        """
        return self.find_by_name("start")
    
    @_cactus_class_method_exception_handle
    def find_by_name(self, name: str):
        """
        This iterates over self.class_data["data"] and finds the Position
        instance with the name specifies, and returns it's index.
        """
        for index, position in enumerate(self.class_data["data"]):
            if self._conditional_lower(position.class_data["name"]) == self._conditional_lower(name):
                return index
        raise LookupError("Could not find position named {0}.".format(name))
