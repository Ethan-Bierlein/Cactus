---
title: Your First Game
site_area: Docs
layout: default
permalink: /Docs/v0.2.x-alpha/FirstGame/
---

# Imports
It's super easy to import Cactus into your project. Once you've added `Cactus/cactus` to your `PYTHONPATH`, this is all you need to do:

    import cactus
    
# Creating a `cactus.Position` instance
A `cactus.Position` instance stores relevant data about a position on a `cactus.Flowchart`. For reference, here's a list of the `cactus.Flowchart` attributes.

* `"name"` - The position's name.
* `"desc_enter"` - The description to display when the player "enters" the position.
* `"desc_exit"` - The description to display when the player "exits" the position.
* `"choices"` - A dictionary of choices representing other positions on the flowchart. The key is what the user enters, and the value is the reference key to the other position in the flowchart.

Here's how a simple `cactus.Position` instance is structured:

    cactus.Position({
        "name":       "start",
        "desc_enter": "Description on enter.",
        "desc_exit":  "Description on exit.",
        "choices": {
            "choice1": "1",
            "choice2": "2"
        }
    })
    
# Creating a `cactus.Flowchart` instance
Flowcharts are essential to Cactus. Flowcharts are how you stucture the "map" that the player of your game will traverse. For reference, here's a list of the `cactus.Flowchart` attributes.

* `"data"` - Stores the actual flowchart data as a dictionary.

Here's how a simple `Flowchart` instance is structured.

    FLOWCHART = cactus.Flowchart({
        "data": {
            "position_name": cactus.Position(
                ...
            )
        }
    })
    
# Creating a `cactus.Game` instance
The `cactus.Game` class stores general data about your game that isn't relevant to flowcharts or positions. The `cactus.Game` class is also where event handlers and global commands are stored. For reference, here's a list of the `cactus.Game` attributes.

* `"name"` - The game's name.
* `"desc"` - The game's description.
* `"prompt"` - The prompt to be used for entering commands.
* `"invalid_input_msg"` - The message to be displayed when the user enters invalid input.
* `"flowchart"` - The flowchart instance that has been created.
* `"case_sensitive"` - If this is `False`, then all user input, and certain attribute values a converted to lowercase. If it's `True`, then none of that happens.
* `"allow_help"` - If this is `True`, then the user can obtain help.
* `"about_text"` - The game's about text, including the reqiuired attribution text.
* `"event_handlers"` - A dictionary of the event handlers and their corresponding functions.
* `"global_commands"` - A dictionary of commands that can be executed anywhere, and their corresponding functions.

Here's how a simple `cactus.Game` instance is structured.

    GAME = cactus.Game({
        "name":              "Game Name",
        "desc":              "Game Description",
        "prompt":            "> ",
        "invalid_input_msg": "Invalid input",
        "flowchart":         FLOWCHART,
        "case_sensitive":    False,
        "allow_help":        True,
        "about_text":        "Write about your game here.",
        "event_handlers": {
            "position.Name Goes Here 1.enter.after": exit,
            "position.Name Goes Here 2.enter.after": exit
        },
        "global_commands": {
            "exit": exit
        }
    })

# Running your game
Once you've done all of the above, you're ready to play your game. Assuming you've created an instance of `cactus.Game`, named it `GAME`, and everything checks out, all you need to do is the below:

    GAME.play_game()

<!--
TODO: Add section describing event handlers.

# Event handlers
...
-->
