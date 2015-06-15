from .flowchart import Flowchart
from .errors import _cactus_class_method_exception_handle

class Game(object):
    """
    Stores general data about the game. A Game instance
    contains the following attributes:
    
        class_data["name"]              - The name of the game.
        class_data["desc"]              - The game's description.
        class_data["prompt"]            - The global prompt to be used.
        class_data["invalid_input_msg"] - A message to print if user enters invalid input.
        class_data["flowchart"]         - The game's flowchart flowchart, a Flowchart instance.
        class_data["case_sensitive"]    - If commands, event handlers, and room names should be case sensitive.
        class_data["allow_help"]        - If the game should print out the choices for the user or not.
        class_data["about_text"]        - The text to be printed out when the user types the `about` command.
        class_data["event_handlers"]    - A dictionary of optional event handlers.
    """
    def __init__(self, class_data: dict):
        self.class_data       = class_data
        self.class_data["flowchart"]._set_game(self)
        self.position         = self.class_data["flowchart"].find_start()
        self._last_position   = None
        self._check_class_data()
        
        for key, position in self.class_data["flowchart"].class_data["data"].items():
            position._set_game(self)
        
    @_cactus_class_method_exception_handle
    def _check_class_data(self):
        """
        Iterate over the contained class data in self.class_data
        and make sure that it's valid.
        """
        self._evaluate_possible_choices()
        
        CLASS_DATA_KEYS_TYPES = [
            ["name", str], ["desc", str], ["prompt", str], ["invalid_input_msg", str],
            ["flowchart", Flowchart], ["case_sensitive", bool], ["allow_help", bool], ["about_text", str],
            ["event_handlers", dict]
        ]
        CLASS_DATA_KEYS       = [
            "name", "desc", "prompt", "invalid_input_msg",
            "flowchart", "case_sensitive", "allow_help", "about_text",
            "event_handlers"
        ]
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
    def _handle_event(self, event_name: str):
        """
        Calls _run_handled_event with context-specific
        arguments.
        """
        self._run_handled_event("game." + event_name)
        
        self._check_class_data()
        self.class_data["flowchart"]._check_class_data()
        for key, position in self.class_data["flowchart"].class_data["data"].items():
            position._check_class_data()
    
    @_cactus_class_method_exception_handle
    def _run_handled_event(self, event_name: str):
        """
        Looks for the event and runs it, if it is there.
        """
        event_data = event_name.split(".")
        
        if event_name in self.conditional_lower_list(self.class_data["event_handlers"]):
            current_location_name = self.class_data["flowchart"].class_data["data"][self.position].class_data["name"]
            if event_data[0] == "game" or (event_data[0] == "position" and self.conditional_lower(current_location_name) == self.conditional_lower(event_data[1])):
                event_handlers_lowered_keys = self.conditional_lower_dict_keys(self.class_data["event_handlers"])
                function                    = event_handlers_lowered_keys[event_name]
                if function != None:
                    function()
    
    @_cactus_class_method_exception_handle
    def conditional_lower(self, text: str):
        """
        It performs the equivalent of the .lower() method
        on the string, only if case should be ignored.
        """
        if self.class_data["case_sensitive"]:
            return text
        else:
            return text.lower()
        
    @_cactus_class_method_exception_handle
    def conditional_lower_list(self, input_data: list):
        """
        Performs `conditional_lower()` on all of the
        items of the list.
        """
        output_data = []
        for item in input_data:
            output_data.append(self.conditional_lower(item))
        
        return output_data
        
    @_cactus_class_method_exception_handle
    def conditional_lower_dict_keys(self, input_data: dict):
        output_data = {}
        for key, value in input_data.items():
            output_data[self.conditional_lower(key)] = value
        
        return output_data
            
    @_cactus_class_method_exception_handle
    def _evaluate_possible_choices(self):
        """
        Evaluates the possible choices in each Position
        and determines if the referenced indexes for each
        choice are valid.
        """
        flowchart_data = self.class_data["flowchart"].class_data["data"]
        for key, position in flowchart_data.items():
            for key, value in position.class_data["choices"].items():
                if value in flowchart_data:
                    continue
                else:
                    raise ValueError("Invalid reference index.")
        
    @_cactus_class_method_exception_handle
    def play_game(self):
        """
        Start playing the user-created game.
        """
        self._handle_event("intro_msg.before")
        print(self.class_data["name"])
        print(self.class_data["desc"])
        print("Special commands: \"help\", \"about\".")
        self._handle_event("intro_msg.after")
        
        while True:
            position_data = self.class_data["flowchart"].class_data["data"][self.position]
            choices       = position_data.class_data["choices"]
            
            if self.position != self._last_position:
                position_data.enter()
            
            self._handle_event("prompt.before")
            user_input = input(self.class_data["prompt"])
            self._handle_event("prompt.after")
            
            cached_position = self.position  # In case `self.position` gets changed below.
            
            if self.conditional_lower(user_input) in self.conditional_lower_list(choices):
                self._handle_event("handle_valid_command.before")
                self._handle_event("position." + position_data.class_data["name"] + ".command." + user_input + ".before")
                self.position = self.conditional_lower_dict_keys(choices)[self.conditional_lower(user_input)]
                if self.position != self._last_position:
                    position_data.exit()
                self._handle_event("position." + position_data.class_data["name"] + ".command." + user_input + ".after")
                self._handle_event("handle_valid_command.after")
                
            elif self.conditional_lower(user_input) == "help" and self.class_data["allow_help"]:
                self._handle_event("handle_help.before")
                print("You have the following choices:")
                if len(position_data.class_data["choices"]) != 0:
                    print(
                        " - " + "\n - ".join([key for key, value in position_data.class_data["choices"].items()])
                    )
                print(
                    " - " + "\n - ".join(["Help", "About"])
                )
                self._handle_event("handle_help.after")
                
            elif self.conditional_lower(user_input) == "about":
                self._handle_event("handle_about.before")
                print(self.class_data["about_text"])
                print("This product includes software developed by The Cactus Project (http://shearofdoom.github.io/Cactus/) and its contributors.")
                self._handle_event("handle_about.after")
                
            else:
                self._handle_event("handle_incorrect_command.before")
                print(self.class_data["invalid_input_msg"])
                self._handle_event("handle_incorrect_command.after")
            
            self._last_position = cached_position
