class MainGame(object):
    """
    Stores general data about the game. A MainGame instance
    contains the following attributes.
    
        class_data["name"]              - The name of the game.
        class_data["desc"]              - The game's description.
        class_data["prompt"]            - The global prompt to be used.
        class_data["invalid_input_msg"] - A message to print if user enters invalid input.
        class_data["map"]               - The game's map data, a GameMap instance.
        class_data["should_lower_text"] - The option to lower text or not.
        class_data["allow_help"]        - If the game should print out the choices for the user or not.
        class_data["about_text"]        - The text to be printed out when the user types the `about` command.
        class_data["event_handlers"]    - A dictionary of optional event handlers.
    """
    def __init__(self, class_data: dict):
        self.class_data        = class_data
        self.class_data["map"].set_game(self)
        self.map_start         = self.class_data["map"].find_start()
        self.map_position      = self.map_start
        self.last_map_position = None
        
        for map_position in self.class_data["map"].class_data["data"]:
            map_position.set_game(self)
        
    def _handle_event(self, event_name: str):
        """
        Calls _run_handled_event with context-specific
        arguments.
        """
        self._run_handled_event("game." + event_name)
        
    def _run_handled_event(self, event_name: str):
        """
        Looks for the event and runs it, if it is there.
        """
        event_data = event_name.split(".")
        
        if event_name in self.class_data["event_handlers"]:
            print(self.class_data["map"].class_data["data"][self.map_position].class_data["name"])
            if event_data[0] == "game" or (event_data[0] == "map_position" and self._conditional_lower(self.class_data["map"].class_data["data"][self.map_position].class_data["name"]) == event_data[1]):
                function = self.class_data["event_handlers"][event_name]
                if function != None:
                    function()
        
    def _conditional_lower(self, text: str):
        """
        It performs the equivalent of the .lower() method
        on the string, only if case should be ignored.
        """
        if self.class_data["should_lower_text"]:
            return text.lower()
        else:
            return text
            
    def _evaluate_possible_choices(self):
        """
        Evaluates the possible choices in each MapPosition
        and determines if the referenced indexes for each
        choice are valid.
        """
        map_data = self.class_data["map"].class_data["data"]
        for position in map_data:
            for key, value in position.class_data["choices"].items():
                if value <= len(map_data) - 1:
                    continue
                else:
                    raise ValueError("Invalid reference index.")
        
    def play_game(self):
        """
        Start playing the user-created game.
        """
        self._evaluate_possible_choices()
        self._handle_event("intro_msg.before")
        print(self.class_data["name"])
        print(self.class_data["desc"])
        print("Special commands: \"help\", \"about\".")
        self._handle_event("intro_msg.after")
        
        while True:
            map_position_data = self.class_data["map"].class_data["data"][self.map_position]
            choices           = map_position_data.class_data["choices"]
            
            if self.map_position != self.last_map_position:
                map_position_data.position_enter()
            
            self._handle_event("prompt.before")
            user_input = input(self.class_data["prompt"])
            self._handle_event("prompt.after")
            
            cached_map_position = self.map_position  # In case `self.map_position` gets changed below.
            
            if self._conditional_lower(user_input) in choices:
                self._handle_event("handle_valid_command.before")
                self._handle_event("map_position." + map_position_data.class_data["name"] + ".command." + self._conditional_lower(user_input) + ".before")
                self.map_position = choices[self._conditional_lower(user_input)]
                map_position_data.position_exit()
                self._handle_event("map_position." + map_position_data.class_data["name"] + ".command." + self._conditional_lower(user_input) + ".after")
                self._handle_event("handle_valid_command.after")
                
            elif self._conditional_lower(user_input) == "help" and self.class_data["should_lower_text"]:
                self._handle_event("handle_help.before")
                print("You have the following choices:")
                print(
                    " - " + "\n - ".join([key for key, value in map_position_data.choices.items()])
                )
                self._handle_event("handle_help.after")
                
            elif self._conditional_lower(user_input) == "about":
                self._handle_event("handle_about.before")
                print(self.class_data["about_text"])
                print("This product includes software developed by The Cactus Project (http://shearofdoom.github.io/Cactus/) and its contributors.")
                self._handle_event("handle_about.after")
                
            else:
                self._handle_event("handle_incorrect_command.before")
                print(self.class_data["invalid_input_msg"])
                self._handle_event("handle_incorrect_command.after")
            
            self.last_map_position = cached_map_position
