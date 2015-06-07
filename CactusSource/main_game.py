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
    """
    def __init__(self, name: str, desc: str, prompt: str, invalid_input_msg: str, map, should_lower_text: bool):
        self.name              = name
        self.desc              = desc
        self.prompt            = prompt
        self.invalid_input_msg = invalid_input_msg
        self.map               = map
        self.should_lower_text = should_lower_text
        self.map_start         = self.map.find_start(self.should_lower_text)
        self.map_position      = self.map_start
        
    def _conditional_lower(self, text: str):
        if self.should_lower_text:
            return text.lower()
        else:
            return text
        
    def play_game(self):
        """
        Start playing the user-created game.
        """
        while True:
            map_position_data = self.map.data[self.map_position]
            choices           = map_position_data.choices
            
            map_position_data.position_enter()
            user_input = input(self.prompt)
            
            if self._conditional_lower(user_input) in choices:
                self.map_position = choices[self._conditional_lower(user_input)]
                map_position_data.position_exit()
            else:
                print(self.invalid_input_msg)
