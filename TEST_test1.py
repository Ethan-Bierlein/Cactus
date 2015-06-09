from sys import exit
from CactusSource.map_position import MapPosition
from CactusSource.game_map import GameMap
from CactusSource.main_game import MainGame


GAME_MAP = GameMap({
    "data": [
        MapPosition({
            "name": "start",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {
                "choice1": 1,
                "choice2": 2
            }
        }),
        MapPosition({
            "name": "Name Goes Here 1",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {}
        }),
        MapPosition({
            "name": "Name Goes Here 2",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {}
        })
    ]
})


MAIN_GAME = MainGame({
    "name": "Game Name",
    "desc": "Game Description",
    "prompt": "> ",
    "invalid_input_msg": "Invalid input",
    "map": GAME_MAP,
    "case_sensitive": False,
    "allow_help": True,
    "about_text": "Write about your game here.",
    "event_handlers": {
        "map_position.name goes here 1.enter.after": exit,
        "map_position.name goes here 2.enter.after": exit
    }
})


MAIN_GAME.play_game()
