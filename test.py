<<<<<<< HEAD
from sys import exit 
from CactusSource.map_position import MapPosition 
from CactusSource.game_map import GameMap 
from CactusSource.main_game import MainGame 
=======

from sys import exit
from CactusSource.map_position import MapPosition
from CactusSource.game_map import GameMap
from CactusSource.main_game import MainGame
>>>>>>> cd43e3bd0b3776d9b913ff4e5b94030db4503461


game_map = GameMap([
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


main_game = MainGame(
    "Test Game",
    "Welcome to the simple test game.",
    "> ",
    "Uh-oh! Wrong input!",
    game_map,
    True,
    True,
    "This is what the game is all about",
    {
        "map_position.right.enter.after": exit,
        "map_position.left.enter.after": exit
    }
)


main_game.play_game()
