---
title: Your First Game
site_area: Docs
layout: default
permalink: /Docs/v0.1.0-alpha/FirstGame/
---

## Includes:

First of all, we need to include the needed items:

    from CactusSource.map_position import MapPosition
    from CactusSource.game_map import GameMap
    from CactusSource.main_game import MainGame

## Creating a `GameMap` Instance:

After that, we want to create a map for our game. A `GameMap` instance has a list of *map positions*,

Unlike a conventional map that displays the location of items in space, a Cactus map is more like a flowchart. It describes the possible paths that the user can take by diving the map into *positions,* which have links to other positions.

Each position has a fixed set of choices (commands) that the user can take. Each choice moves the user to another position, although you can just specify the same position to stay at the same position.

 Let's look at an example game map:

    game_map = GameMap([
        MapPosition(
            "Start",
            "Welcome to the start!",
            "Now leaving the start.",
            {
                "left": 1,
                "right": 2
            }
        ),
        MapPosition(
            "Left",
            "You took the left path and died.",
            "",
            {},
        function=exit
        ),
        MapPosition(
            "Right",
            "You took the right path and lived!",
            "",
            {},
            function=exit
        )
    ])

As you can see, we have three positions (`MapPositions`) in this map. We passed all three of these to the initialiser function in a list.

Let's dissect the first `MapPosition`:

    MapPosition(
      "Start",
      "Welcome to the start!",
      "Now leaving the start.",
      {
        "left": 1,
        "right": 2
      }
    )

It has the following attributes:

- The name (`Start`)
- The enter text (`Welcome to the start!`)
- The exit text (`Now leaving the start.`)
- Choices (a dictionary of two choices: `left` and `right`)
    - Each choice has a number that points to the room the user will go to next if they choose that option (in this case, `left` goes to the `Left` room and `right` goes to the `Right` room)

## Creating the Main Game:

    main_game = MainGame(
      "Test Game",
      "Welcome to the simple test game.",
      "> ",
      "Uh-oh! Wrong input!",
      game_map,
      True
    )

It has the following attributes:

- The name (`Test Game`)
- The enter text (`Welcome to the simple test game.`)
- The prompt that will be displayed when asking the user for input (`> `)
- The text for when a user enters incorrect text (`Uh-oh! Wrong Input!`)
- The game map (`game_map`)
- If it should ignore case (`True`)

## Starting the Game:

All you have to run is this:

    main_game.play_game()
