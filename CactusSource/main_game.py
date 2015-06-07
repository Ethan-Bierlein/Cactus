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
    """
    def __init__(self, name: str, desc: str, prompt: str, invalid_input_msg: str, map, should_lower_text: bool, allow_help: bool, about_text: str):
        self.name              = name
        self.desc              = desc
        self.prompt            = prompt
        self.invalid_input_msg = invalid_input_msg
        self.map               = map
        self.should_lower_text = should_lower_text
        self.allow_help        = allow_help
        self.about_text        = about_text
        self.map_start         = self.map.find_start(self.should_lower_text)
        self.map_position      = self.map_start
        self.last_map_position = None
        
    def _conditional_lower(self, text: str):
        if self.should_lower_text:
            return text.lower()
        else:
            return text
        
    def play_game(self):
        """
        Start playing the user-created game.
        """
        print(self.name)
        print(self.desc)
        print("Special commands: `help`, `about`.")
        
        while True:
            map_position_data = self.map.data[self.map_position]
            choices           = map_position_data.choices
            
            if not self.map_position == self.last_map_position:
                map_position_data.position_enter(self.allow_help)
            
            user_input = input(self.prompt)
            
            if self._conditional_lower(user_input) in choices:
                self.map_position = choices[self._conditional_lower(user_input)]
                map_position_data.position_exit()
            elif self._conditional_lower(user_input) == "help" and self.allow_help:
                print("You have the following choices:")
                print(
                    ' - ' + '\n - '.join([key for key, value in map_position_data.choices.items()])
                )
            elif self._conditional_lower(user_input) == "about":
                print(self.about_text)
                print("This product includes software developed by The Cactus Project (http://shearofdoom.github.io/Cactus/) and its contributors.")
            else:
                print(self.invalid_input_msg)
            
            self.last_map_position = self.map_position
