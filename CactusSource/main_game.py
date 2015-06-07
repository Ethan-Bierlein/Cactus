class MainGame(object):
    """
    Stores general data about the game. A MainGame instance
    contains the following attributes.
    
        name              - The name of the game.
        desc              - The game's description.
        prompt            - The global prompt to be used.
        invalid_input_msg - A message to print if user enters invalid input.
        map               - The game's map data, a GameMap instance.
        should_lower_text - The option to lower text or not.
        allow_help        - If the game should print out the choices for the user or not.
        about_text        - The text to be printed out when the user types the `about` command.
        event_handlers    - A dictionary of optional event handlers.
    """
    def __init__(self, name: str, desc: str, prompt: str, invalid_input_msg: str, map, should_lower_text: bool, allow_help: bool, about_text: str, event_handlers):
        self.name              = name
        self.desc              = desc
        self.prompt            = prompt
        self.invalid_input_msg = invalid_input_msg
        self.map               = map
        
        self.map.set_game(self)
        
        self.should_lower_text = should_lower_text
        self.allow_help        = allow_help
        self.about_text        = about_text
        self.event_handlers    = event_handlers
        self.map_start         = self.map.find_start()
        self.map_position      = self.map_start
        self.last_map_position = None
        
        for map_position in self.map.data:
            map_position.set_game(self)
        
    def _handle_event(self, event_name: str):
        self._run_handled_event("game." + event_name)
        
    def _run_handled_event(self, event_name: str):
        """
        Looks for the event and runs it, if it is there.
        """
        event_data = event_name.split(".")
        
        if event_data[0] == "game":
            if event_name in self.event_handlers:
                function = self.event_handlers[event_name]
                if function != None:
                    function()
        elif event_data[0] == "map_position" and self.map.find_by_name(event_data[1]) != -1:
            map_position = self.map.data[self.map.find_by_name(event_data[1])]
            
            if event_name in map_position.event_handlers:
                function = map_position.event_handlers[event_name]
                if function != None:
                    function()
        
    def _conditional_lower(self, text: str):
        if self.should_lower_text:
            return text.lower()
        else:
            return text
        
    def play_game(self):
        """
        Start playing the user-created game.
        """
        self._handle_event("intro_msg.b")
        print(self.name)
        print(self.desc)
        print("Special commands: `help`, `about`.")
        self._handle_event("intro_msg.a")
        
        while True:
            map_position_data = self.map.data[self.map_position]
            choices           = map_position_data.choices
            
            if self.map_position != self.last_map_position:
                map_position_data.position_enter()
            
            self._handle_event("prompt.b")
            user_input = input(self.prompt)
            self._handle_event("prompt.a")
            
            cached_map_position = self.map_position  # In case `self.map_position` gets changed below.
            
            if self._conditional_lower(user_input) in choices:
                self._handle_event("handle_valid_command.b")
                self._handle_event("map_position." + map_position_data.name + ".command." + self._conditional_lower(user_input) + ".b")
                self.map_position = choices[self._conditional_lower(user_input)]
                map_position_data.position_exit()
                self._handle_event("map_position." + map_position_data.name + ".command." + self._conditional_lower(user_input) + ".a")
                self._handle_event("handle_valid_command.a")
            elif self._conditional_lower(user_input) == "help" and self.allow_help:
                self._handle_event("handle_help.b")
                print("You have the following choices:")
                print(
                    ' - ' + '\n - '.join([key for key, value in map_position_data.choices.items()])
                )
                self._handle_event("handle_help.a")
            elif self._conditional_lower(user_input) == "about":
                self._handle_event("handle_about.b")
                print(self.about_text)
                print("This product includes software developed by The Cactus Project (http://shearofdoom.github.io/Cactus/) and its contributors.")
                self._handle_event("handle_about.a")
            else:
                self._handle_event("handle_incorrect_command.b")
                print(self.invalid_input_msg)
                self._handle_event("handle_incorrect_command.a")
            
            self.last_map_position = cached_map_position
