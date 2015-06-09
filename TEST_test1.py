from sys import exit
from CactusSource.cactus_position import CactusPosition
from CactusSource.cactus_map import CactusMap
from CactusSource.cactus_game import CactusGame


game_map = CactusMap({
    "data": [
        CactusPosition({
            "name": "start",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {
                "choice1": 1,
                "choice2": 2
            }
        }),
        CactusPosition({
            "name": "Name Goes Here 1",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {}
        }),
        CactusPosition({
            "name": "Name Goes Here 2",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {}
        })
    ]
})


cactus_game = CactusGame({
    "name": "Game Name",
    "desc": "Game Description",
    "prompt": "> ",
    "invalid_input_msg": "Invalid input",
    "map": game_map,
    "case_sensitive": False,
    "allow_help": True,
    "about_text": "Write about your game here.",
    "event_handlers": {
        "cactus_position.name goes here 1.enter.after": exit,
        "cactus_position.name goes here 2.enter.after": exit
    }
})


cactus_game.play_game()
