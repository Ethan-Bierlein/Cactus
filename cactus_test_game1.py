from sys import exit
from CactusSource.map_position import MapPosition
from CactusSource.game_map import GameMap
from CactusSource.main_game import MainGame


GAME_MAP = GameMap([
    MapPosition(
        "Start",
        "You are currently standing in the middle of the desert, there is a cactus at your side.",
        "As you leave the start, you wave goodbye to your cactus friend.\n",
        {
            "north": 1,
            "south": 2,
            "east": 3,
            "west": 4
        }
    ),
    MapPosition(
        "Northern Plains",
        "There are large mountains ahead in your view.",
        "You have continued on from the Northern Plains.\n",
        {
            "north": 5
        }
    ),
    MapPosition(
        "Southern Gravel Lands",
        "Here you find vast empty plains of gravel.",
        "You have continued on from the Southern Gravel Lands\n",
        {
            "north": 1
        }
    ),
    MapPosition(
        "Eastern Sand Dunes",
        "Ahead lies vast amounts of large looming sand dunes, blowing in the wind.",
        "You have continued on from the Eastern Sand Dunes.\n",
        {
            "south": 2
        }
    ),
    MapPosition(
        "Western Rocky Plains",
        "The ground lies littered with sharp, small rocks. You watch your step as you walk.",
        "You have continued on from the Western Rocky Plains.\n",
        {
            "east": 3
        }
    ),
    MapPosition(
        "Cave Entrance",
        "A cave lies ahead. It is dark, so you pull out a match.",
        "You have continued deeper into the cave.\n",
        {
            "left": 6,
            "right": 7
        }
    ),
    MapPosition(
        "Left Cave Tunnel",
        "You went left and found a bear. That bear then promptly ate you.",
        "",
        {},
    ),
    MapPosition(
        "Right Cave Tunnel",
        "You went right and found a magical portal. You went home. Yay.",
        "",
        {},
    )
])


MAIN_GAME = MainGame(
    "In The Desert",
    "Welcome to \"In The Desert\"",
    "-- ",
    "You've entered the wrong command! Try again.",
    GAME_MAP,
    True,
    True,
    "You are a traveler who has lost his way in the desert, and your goal is to find a way home. Good luck.",
    {
        "map_position.left cave tunnel.enter.after": exit,
        "map_position.right cave tunnel.enter.after": exit,
    }
)


MAIN_GAME.play_game()
