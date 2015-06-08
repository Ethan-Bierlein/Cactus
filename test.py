from sys import exit 
from CactusSource.map_position import MapPosition 
from CactusSource.game_map import GameMap 
from CactusSource.main_game import MainGame 


GAME_MAP = GameMap([ 
    MapPosition( 
        "Start", 
        "Welcome to the start!", 
        "Now leaving the start.", 
        { 
            "left": 1, 
            "right": 2, 
        } 
    ), 
    MapPosition( 
        "Left", 
        "You took the left path and died.", 
        "", 
        {} 
    ), 
    MapPosition( 
        "Right", 
        "You took the right path and lived!", 
        "", 
        {} 
    ), 
]) 


MAIN_GAME = MainGame( 
    "Test Game", 
    "Welcome to the simple test game.", 
    "> ", 
    "Uh-oh! Wrong input!", 
    GAME_MAP, 
    True, 
    True, 
    "This is what the game is all about", 
    { 
        "map_position.right.enter.after": exit, 
        "map_position.left.enter.after": exit 
    } 
) 


MAIN_GAME.play_game()
