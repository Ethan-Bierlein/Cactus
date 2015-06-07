class MapPosition(object):
    """
    Stores general data about a position on the
    map. A MapPosition instance contains the
    following data.
    
        name       - The name of the MapPosition.
        desc_enter - A description of the MapPosition displayed when the player enters.
        desc_exit  - A description of the MapPosition displayed when the player exits.
        choices    - A dictionary referencing other possible choices, e.g, indexes in the map.
        event_handlers    - A dictionary of optional event handlers.
    """
    def __init__(self, name: str, desc_enter: str, desc_exit: str, choices: dict, event_handlers):
        self.name           = name
        self.desc_enter     = desc_enter
        self.desc_exit      = desc_exit
        self.choices        = choices
        self.event_handlers = event_handlers
        self.game           = None
        
    def set_game(self, game):
        """
        Sets the game instance this object belongs to.
        """
        self.game = game
        
    def _handle_event(self, event_name: str):
        self.game._run_handled_event("map_position." + self.game._conditional_lower(self.name) + "." + event_name)
        
    def position_enter(self):
        """
        Output the various data associated with a MapPosition when
        the player enters the MapPosition.
        """
        self._handle_event("enter.b")
        if self.choices != {}:
            if self.game.allow_help:
                print(
                    "{0}: {1} Choices: {2}".format(
                        self.name,
                        self.desc_enter,
                        ', '.join([key for key, value in self.choices.items()])
                    )
                )
            else:
                print(
                    "{0}: {1}".format(
                        self.name,
                        self.desc_enter
                    )
                )
        else:
            print(
                "{0}: {1}".format(
                    self.name,
                    self.desc_enter
                )
            )
        
        self._handle_event("enter.a")
            
    def position_exit(self):
        """
        Output the various data associated with a MapPosition when
        the player exits the MapPosition.
        """
        self._handle_event("exit.b")
        print(self.desc_exit)
        self._handle_event("exit.a")
