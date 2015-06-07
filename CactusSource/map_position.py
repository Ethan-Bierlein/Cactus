class MapPosition(object):
    """
    Stores general data about a position on the
    map. A MapPosition instance contains the
    following data.
    
        name       - The name of the MapPosition.
        desc_enter - A description of the MapPosition displayed when the player enters.
        desc_exit  - A description of the MapPosition displayed when the player exits.
        choices    - A dictionary referencing other possible choices, e.g, indexes in the map.
        function   - An optional function to be run after desc_enter is displayed.
    """
    def __init__(self, name: str, desc_enter: str, desc_exit: str, choices: dict, function=None):
        self.name       = name
        self.desc_enter = desc_enter
        self.desc_exit  = desc_exit
        self.choices    = choices
        self.function   = function
        
    def position_enter(self):
        """
        Output the various data associated with a MapPosition when
        the player enters the MapPosition.
        """
        if self.choices != {}:
            print(
                "{0}: {1} {2}".format(
                    self.name,
                    "\n\n" + self.desc_enter,
                    "\n\n" + "Choices: " + ', '.join([key for key, value in self.choices.items()])
                )
            )
        else:
            print(
                "{0}: {1}".format(
                    self.name,
                    "\n\n" + self.desc_enter,
                )
            )
        if self.function is not None:
            self.function()
            
    def position_exit(self):
        """
        Output the various data associated with a MapPosition when
        the player exits the MapPosition.
        """
        print("\n\n" + self.desc_exit + "\n\n")
