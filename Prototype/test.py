import prototype as cactus
from sys import exit

GAME_MAP = cactus.GameMap([
	cactus.MapPosition(
		"Start",
		"Welcome to the test!",
		{
			"left":  1,
			"right": 2,
		}
	),
	cactus.MapPosition(
		"Left",
		"You took the left path and lived!",
		{},
		function=exit
	),
	cactus.MapPosition(
		"Right",
		"You took the right path and died!",
		{},
		function=exit,
	)
])

GAME = cactus.MainGame(
	"Test Game",
	"This is a simple test game! Yay!",
	"> ",
	GAME_MAP
)

GAME.play_game()