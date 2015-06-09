class Position(object):
    """
    Stores general data about a position on the
    flowchart. A Position instance contains the
    following data.
    
        class_data["name"]       - The name of the Position.
        class_data["desc_enter"] - A description of the Position displayed when the player enters.
        class_data["desc_exit"]  - A description of the Position displayed when the player exits.
        class_data["choices"]    - A dictionary referencing other possible choices, e.g, indexes in the flowchart.
    """
    def __init__(self, class_data: dict):
        self.class_data         = class_data
        self.game               = None
        self._conditional_lower = None
        
    def set_game(self, game):
        """
        Sets the game instance this object belongs to.
        """
        self.game               = game
        self._conditional_lower = self.game._conditional_lower
        
    def _handle_event(self, event_name: str):
        """
        Calls Game._run_handled_event with
        context-specific arguments.
        """
        self.game._run_handled_event("position." + self._conditional_lower(self.class_data["name"]) + "." + event_name)
        
    def position_enter(self):
        """
        Output the various data associated with a Position when
        the player enters the Position.
        """
        self._handle_event("enter.before")
        if self.class_data["choices"] != {}:
            if self.game.class_data["allow_help"]:
                print(
                    "{0}: {1} Choices: {2}".format(
                        self.class_data["name"],
                        self.class_data["desc_enter"],
                        ", ".join([key for key, value in self.class_data["choices"].items()])
                    )
                )
            else:
                print(
                    "{0}: {1}".format(
                        self.class_data["name"],
                        self.class_data["desc_enter"]
                    )
                )
        else:
            print(
                "{0}: {1}".format(
                    self.class_data["name"],
                    self.class_data["desc_enter"]
                )
            )
        
        self._handle_event("enter.after")
            
    def position_exit(self):
        """
        Output the various data associated with a Position when
        the player exits the Position.
        """
        self._handle_event("exit.before")
        print(self.class_data["desc_exit"])
        self._handle_event("exit.after")
